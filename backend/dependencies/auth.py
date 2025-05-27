# backend/dependencies/auth.py

from fastapi import Depends, HTTPException, Request
from sqlalchemy.orm import Session
from database import get_db

# Модель пользователя и связь «пользователь–роль»
from models.user import User, UserRole
# Модель роли лежит в models/organizations.py
from models.organizations import Role


def get_current_user(request: Request) -> str:
    """
    Достаёт user_id из request.state, который выставляет ваш AuthMiddleware.
    """
    user_id = getattr(request.state, "user_id", None)
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return user_id


def get_current_user_with_roles(
    user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> User:
    """
    Возвращает объект User вместе со списком ролей в атрибуте .role_names
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Загружаем user_roles и собираем названия ролей через relationship на Role
    role_names = []
    for ur in db.query(UserRole).filter(UserRole.user_id == user_id).all():
        # UserRole.role — это связь на Role
        if ur.role:
            role_names.append(ur.role.role)
    setattr(user, "role_names", role_names)

    return user
