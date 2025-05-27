from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from database import get_db
from models.user import User, UserRole
from models.organizations import Role

def get_current_user_with_roles(user_id: str = Depends(get_current_user), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # ищем роли
    user_roles = db.query(UserRole).filter_by(user_id=user.id).all()
    role_names = db.query(Role.role).filter(Role.id.in_([r.role_id for r in user_roles])).all()
    role_names = [r[0] for r in role_names]  # вытаскиваем строковые названия

    user.role_names = role_names  # просто список: ["admin", "manager", ...]
    return user
