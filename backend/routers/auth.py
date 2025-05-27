from fastapi import APIRouter, HTTPException, Depends, Request, Response
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from schemas.user import UserCreate, UserUpdate, UserRead, UserLogin
from utils.hashing import hash_password
from sqlalchemy.exc import IntegrityError
from utils.ulid_generator import generate_ulid
from datetime import datetime
from utils.logger import log_pdata_changes
from utils.auth import create_access_token
from fastapi.responses import JSONResponse
from dependencies.auth import get_current_user
from fastapi import Response
from utils.password import verify_password
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from database import get_db
from models.agreement_type import AgreementType
from models.user_agreements import UserAgreement
import uuid

router = APIRouter()
def generate_public_slug():
    return uuid.uuid4().hex[:12]


@router.post("/register")
def register(user_data: UserCreate, request: Request, db: Session = Depends(get_db)):
    actor = getattr(request.state, "user_id", None) or "self"
    if not (user_data.agreed_offer and user_data.agreed_personal and user_data.agreed_policy):
        raise HTTPException(400, "Вы должны принять оферту, согласие на ПД и политику.")
    if getattr(request.state, "user_id", None):
        raise HTTPException(status_code=403, detail="You are already authenticated")
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    new_user = User(
        id = generate_ulid(),
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        created_at=datetime.utcnow(),
        public_slug=generate_public_slug()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    types = { t.name: t.id for t in db.query(AgreementType).all() }
    now = datetime.utcnow()

    ua  = [
      # Оферта
      UserAgreement(
        user_id           = new_user.id,
        agreement_type_id = types["offer"],
        agreed          = True,
        created_at        = now,
        created_by        = new_user.id
      ),
      # ПД
      UserAgreement(
        user_id           = new_user.id,
        agreement_type_id = types["personal_data"],
        agreed          = True,
        created_at        = now,
        created_by        = new_user.id
      ),
      # Политика
      UserAgreement(
        user_id           = new_user.id,
        agreement_type_id = types["policy"],
        agreed          = True,
        created_at        = now,
        created_by        = new_user.id
      ),
      # Рассылка (опционально)
      UserAgreement(
        user_id           = new_user.id,
        agreement_type_id = types["advertisement"],
        agreed          = user_data.agreed_advertisement,
        created_at        = now,
        created_by        = new_user.id
      ),
    ]
    db.add_all(ua)
    db.commit()


    # Логирование создания ПД
    log_pdata_changes(
        db=db,
        old_obj=None,         # для create можно оставить None
        new_obj=new_user,
        user_id=getattr(request.state, "user_id", None) 
    )

    token = create_access_token({"sub": new_user.id})

    response = JSONResponse(content={"message": "User created"})
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="Strict",
        max_age=3600 * 24,
        path="/"
    )
    return response


@router.put("/users/{user_id}")
def update_user(user_id: str, user_data: UserUpdate, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    old_user = deepcopy(user)

    # обновляем только те поля, которые пришли
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(user, key, value)

    log_pdata_changes(
        db=db,
        old_obj=old_user,
        new_obj=user,
        user_id=getattr(request.state, "user_id", None)
    )

    db.commit()
    db.refresh(user)

    return {"message": "User updated", "user_id": user.id}


@router.delete("/users/{user_id}")
def delete_user(user_id: str, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    old_user = deepcopy(user)

    # логируем удаление
    log_pdata_changes(
        db=db,
        old_obj=old_user,
        new_obj=None,
        user_id=getattr(request.state, "user_id", None)  # если временно нет — передавай None
    )

    db.delete(user)
    db.commit()

    return {"message": f"User {user_id} deleted"}


@router.get("/cabinet")
def get_cabinet(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at.isoformat()
    }

    
@router.post("/login")
def login(user_data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Неверные данные для входа")

    access_token = create_access_token({"sub": user.id}, expires_delta=timedelta(hours=1))
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/"
    )

    return {"message": "Login successful"}


@router.post("/logout")
def logout(response: Response):
    """
    Удаляем куку access_token и возвращаем подтверждение.
    """
    response.delete_cookie(key="access_token", path="/")
    return {"message": "Logged out"}