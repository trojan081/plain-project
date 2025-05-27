# 📄 backend/routers/organizations.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

# Авторизация по ролям (возвращает объект User с полями id, role_names и т.п.)
from dependencies.auth import get_current_user_with_roles

# Правильный импорт моделей (именем файла «organizations.py»)
from models.organizations import Organization, OrganizationMember

# Схемы Pydantic для организации и приглашения
from schemas.organization import (
    OrganizationCreate,
    OrganizationRead,
    OrganizationMemberInvite,
    OrganizationMemberRead,
)

from utils.ulid_generator import generate_ulid
from datetime import datetime

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.get("/my", response_model=OrganizationRead)
def get_my_organization(
    user=Depends(get_current_user_with_roles),
    db: Session = Depends(get_db),
):
    member = db.query(OrganizationMember).filter_by(user_id=user.id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Вы не состоите в организации")
    org = db.query(Organization).filter_by(id=member.org_id).first()
    return org


@router.post("/", response_model=OrganizationRead)
def create_organization(
    payload: OrganizationCreate,
    user=Depends(get_current_user_with_roles),
    db: Session = Depends(get_db),
):
    if not any(r in ("admin", "manager") for r in user.role_names):
        raise HTTPException(status_code=403, detail="Недостаточно прав для создания организации")

    org = Organization(
        id=generate_ulid(),
        name=payload.name,
        org_type=payload.org_type,
        inn=payload.inn,
        location=payload.location,
        email=payload.email,
        created_by=user.id,
        updated_by=user.id,
    )
    db.add(org)
    db.commit()
    db.refresh(org)

    # Добавляем создателя как участника
    member = OrganizationMember(
        id=generate_ulid(),
        org_id=org.id,
        user_id=user.id,
        employee_status_id=None,
        created_by=user.id,
        updated_by=user.id,
    )
    db.add(member)
    db.commit()
    return org


@router.post("/invite", response_model=OrganizationMemberRead)
def invite_member(
    payload: OrganizationMemberInvite,
    user=Depends(get_current_user_with_roles),
    db: Session = Depends(get_db),
):
    if not any(r in ("admin", "manager") for r in user.role_names):
        raise HTTPException(status_code=403, detail="Недостаточно прав для приглашения")

    # Находим организацию, где пользователь — участник
    member = db.query(OrganizationMember).filter_by(user_id=user.id).first()
    if not member:
        raise HTTPException(status_code=400, detail="Вы не состоите в организации")

    new_member = OrganizationMember(
        id=generate_ulid(),
        org_id=member.org_id,
        user_id=payload.user_id,
        employee_status_id=None,
        created_by=user.id,
        updated_by=user.id,
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member
