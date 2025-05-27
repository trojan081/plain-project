from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.auth import get_current_user
from database import get_db
from models.user import User
from models.user_info import UserInfo
from models.projects import Project, ProjectInfo, UserProject
from models.organizations import OrganizationMember
from schemas.user_profile import UserProfileResponse, ProjectSummary
from typing import List

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/{public_slug}", response_model=UserProfileResponse)
def get_user_profile(
    public_slug: str,
    db: Session = Depends(get_db),
    current_user_id: str = Depends(get_current_user)
):
    # Ищем пользователя по public_slug
    user = db.query(User).filter(User.public_slug == public_slug).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Последняя запись с ФИО и фото
    user_info = (
        db.query(UserInfo)
        .filter(UserInfo.user_id == user.id)
        .order_by(UserInfo.updated_at.desc())
        .first()
    )

    # Получаем список ID организаций, в которых состоит текущий пользователь
    user_org_ids = db.query(OrganizationMember.org_id).filter_by(user_id=current_user_id).subquery()
    allowed_org_ids = [row[0] for row in db.query(user_org_ids).all()]

    # Получаем проекты пользователя
    projects = (
        db.query(Project, ProjectInfo)
        .join(ProjectInfo, Project.id == ProjectInfo.project_id)
        .join(UserProject, UserProject.project_id == Project.id)
        .filter(UserProject.user_id == user.id)
        .all()
    )

    # Только те, что в общей организации
    visible_projects: List[ProjectSummary] = []
    for proj, info in projects:
        if info.org_id in allowed_org_ids:
            visible_projects.append(ProjectSummary(
                id=proj.id,
                name=proj.name,
                status=info.project_status,
                created_at=proj.created_at,
                location=info.location
            ))

    return UserProfileResponse(
        user_id=user.id,
        public_slug=user.public_slug,
        email=user.email,
        first_name=user_info.first_name if user_info else None,
        last_name=user_info.last_name if user_info else None,
        photo_url=user_info.photo_url if user_info else None,
        fathers_name=user_info.fathers_name if user_info else None,
        phone=user_info.phone if user_info else None,
        position=user_info.position if user_info else None,
        is_friend=False,
        projects=visible_projects
    )
