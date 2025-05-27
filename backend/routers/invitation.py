from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.organizations import OrganizationMember
from models.user import User
from schemas.invitation import InvitationCreate
from dependencies.auth import get_current_user
from datetime import datetime

router = APIRouter(prefix="/invitation", tags=["invitation"])

@router.post("/")
def invite_user(payload: InvitationCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    invited_user = db.query(User).filter_by(email=payload.email).first()
    if not invited_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Проверка на уже существующее участие
    existing = db.query(OrganizationMember).filter_by(user_id=invited_user.id, org_id=payload.org_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Пользователь уже в организации")

    # Добавляем
    member = OrganizationMember(
        user_id=invited_user.id,
        org_id=payload.org_id,
        employee_status_id=2,  # обычный пользователь
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(member)
    db.commit()
    return {"detail": "Пользователь приглашён в организацию"}
