from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from database import get_db
from models.user_info import UserInfo
from schemas.user_info import UserInfoRead, UserInfoUpdate
from utils.logger import log_pdata_changes
from utils.ulid_generator import generate_ulid
from datetime import datetime
from copy import deepcopy
from fastapi import UploadFile, File
import os
from pathlib import Path

router = APIRouter(tags=["user_info"])

@router.get("/user_info", response_model=UserInfoRead)
def read_user_info(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    info = db.query(UserInfo).filter_by(user_id=user_id).order_by(UserInfo.updated_at.desc()).first()
    if not info:
        # возвращаем «пустую» корзину: все поля None
        return UserInfoRead(
            user_id=user_id,
            first_name=None,
            middle_name=None,
            last_name=None,
            fathers_name=None,
            phone=None,
            position=None,
            photo_url=None,
            created_at=datetime.utcnow().isoformat(),
            updated_at=None
        )
    return info


FIELDS_TO_CHECK = (
    "first_name",
    "middle_name",
    "last_name",
    "fathers_name",
    "phone",
    "photo_url",
    "position",
)

@router.put("/user_info", response_model=UserInfoRead)
def update_user_info(
    payload: UserInfoUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    # 1. берём все записи пользователя
    q = db.query(UserInfo).filter_by(user_id=user_id)

    # 2. самая СТАРАЯ запись → её created_at фиксируем
    first_rec   = q.order_by(UserInfo.created_at.asc()).first()
    first_date  = first_rec.created_at if first_rec else datetime.utcnow()

    # 3. самая НОВАЯ запись → используем для логов «было/стало»
    last_rec    = q.order_by(UserInfo.updated_at.desc()).first()
    old_copy    = deepcopy(last_rec) if last_rec else None

    # 4. если данные не изменились - ничего не делаем
    if old_copy:
        unchanged = True
        for field in FIELDS_TO_CHECK:
            old_val = getattr(old_copy, field, None)
            new_val = getattr(payload, field, None)
            if old_val != new_val:
                unchanged = False
                break
        if unchanged:
            return old_copy  # данные те же, просто возвращаем старую запись

    # 5. создаём НОВУЮ строку, копируя прежний created_at
    info = UserInfo(
        user_id     = user_id,
        created_at  = first_date,        # ← фиксируем старую дату
        created_by  = user_id,
        updated_by  = user_id,
        **payload.dict(exclude_unset=True),
    )
    db.add(info)
    db.flush()
    log_pdata_changes(db=db, old_obj=old_copy, new_obj=info, user_id=user_id)

    db.commit()
    db.refresh(info)

    
    return info

UPLOAD_DIR = Path("static/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/user_info/photo", response_model=UserInfoRead)
async def upload_user_photo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user),
):
    from models.pdata_action import PDataAction
    from utils.ulid_generator import generate_ulid
    from shutil import os
    from datetime import datetime

    # Проверяем расширение файла
    ext = file.filename.split(".")[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "gif"}:
        raise HTTPException(status_code=400, detail="Формат файла не поддерживается")

    # Получаем старую запись
    last_info = db.query(UserInfo).filter_by(user_id=user_id).order_by(UserInfo.updated_at.desc()).first()

    if not last_info:
        raise HTTPException(status_code=404, detail="User info not found")

    old_photo_url = last_info.photo_url

    # Создаём новое имя файла
    ulid = generate_ulid()
    filename = f"{user_id}_{ulid}_photo.{ext}"
    file_path = UPLOAD_DIR / filename

    # Сохраняем новое фото
    with file_path.open("wb") as buffer:
        buffer.write(await file.read())

    new_photo_url = f"/static/uploads/{filename}"

    # СОЗДАЁМ новую запись UserInfo, копируя старые данные, но обновляя только photo_url
    new_info = UserInfo(
        user_id=user_id,
        first_name=last_info.first_name,
        middle_name=last_info.middle_name,
        last_name=last_info.last_name,
        fathers_name=last_info.fathers_name,
        phone=last_info.phone,
        position=last_info.position,
        created_at=last_info.created_at,  # сохраняем дату создания
        created_by=user_id,
        updated_by=user_id,
        photo_url=new_photo_url
    )

    db.add(new_info)
    db.flush()

    # Логируем смену фото
    if old_photo_url != new_photo_url:
        db.add(PDataAction(
            id=generate_ulid(),
            event_type="update",
            object_type="user_info",
            object_id=str(new_info.id),
            field="photo_url",
            old_value=old_photo_url,
            new_value=new_photo_url,
            performed_by=user_id,
            performed_at=datetime.utcnow()
        ))

        # Логируем удаление файла
        if old_photo_url:
            db.add(PDataAction(
                id=generate_ulid(),
                event_type="delete_file",
                object_type="file",
                object_id=user_id,
                field="photo_url",
                old_value=old_photo_url,
                new_value=None,
                performed_by=user_id,
                performed_at=datetime.utcnow()
            ))

            # Удаляем старый файл физически
            old_file_path = Path("." + old_photo_url)
            if old_file_path.exists():
                old_file_path.unlink()

    db.commit()
    db.refresh(new_info)

    return new_info