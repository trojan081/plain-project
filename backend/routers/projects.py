from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db, BASE_URL
from models.projects import (
    Project, ProjectInfo, ProjectVersion, UserProject
)
from models.organizations import OrganizationMember
from models.user_info import UserInfo
from models.user import User
from schemas.project import ProjectCreate, ProjectUpdate, ProjectRead
from schemas.project_version import ProjectVersionCreate, ProjectVersionRead
from dependencies.auth import get_current_user, get_current_user_with_roles
from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import aliased
from sqlalchemy import desc

router = APIRouter(prefix="/project", tags=["project"])

# --- Создание проекта ---
@router.post("/", response_model=ProjectRead, summary="Создать проект")
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    new_project = Project(
        name=payload.name,
        created_by=user_id,
        updated_by=user_id
    )
    db.add(new_project)
    db.flush()

    project_info = ProjectInfo(
        project_id=new_project.id, 
        org_id=payload.org_id,
        cad_drafter_id=user_id,
        project_manager=payload.project_manager,
        project_status=payload.project_status,
        area=payload.area,
        location=payload.location,
        regulation_document=payload.regulation_document,
        custom_status=payload.custom_status,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(project_info)

    user_project = UserProject(
        user_id=user_id,
        project_id=new_project.id,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(user_project)

    db.commit()
    db.refresh(new_project)
    db.refresh(project_info)

    return ProjectRead(
        id=new_project.id,
        name=new_project.name,
        created_at=new_project.created_at,
        updated_at=new_project.updated_at,
        created_by=new_project.created_by,
        updated_by=new_project.updated_by,
        location=project_info.location,
        area=project_info.area,
        project_status=project_info.project_status,
        custom_status=project_info.custom_status,
        regulation_document=project_info.regulation_document,
        cad_drafter_id=project_info.cad_drafter_id,
        project_manager=project_info.project_manager,
        org_id=project_info.org_id,
        cad_drafter_name=None,
        cad_drafter_avatar=None
    )

# --- Список проектов с фильтрами ---
@router.get("/", response_model=List[ProjectRead], summary="Список проектов")
def list_projects(
    org_id: Optional[int] = Query(None),
    status_id: Optional[int] = Query(None),
    only_my: Optional[bool] = Query(False),
    limit: Optional[int] = Query(50),
    offset: Optional[int] = Query(0),
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):

    latest_user_info = (
    db.query(UserInfo)
    .distinct(UserInfo.user_id)
    .order_by(UserInfo.user_id, desc(UserInfo.updated_at))
    .subquery()
    )
    UserInfoLatest = aliased(UserInfo, latest_user_info)

    query = (
    db.query(ProjectInfo, Project, UserInfoLatest)
    .join(Project, Project.id == ProjectInfo.project_id)
    .outerjoin(UserInfoLatest, UserInfoLatest.user_id == ProjectInfo.cad_drafter_id)
    )

    if status_id is not None:
        query = query.filter(ProjectInfo.project_status == status_id)

    if only_my:
        query = query.filter(
            (ProjectInfo.cad_drafter_id == user_id) | 
            (ProjectInfo.created_by == user_id)
        )
    else:
        org_ids = db.query(OrganizationMember.org_id).filter_by(user_id=user_id).subquery()
        query = query.filter(ProjectInfo.org_id.in_(org_ids))

    results = query.order_by(ProjectInfo.created_at.desc()).limit(limit).offset(offset).all()

    return [
        ProjectRead(
            id=proj.id,
            name=project.name,
            created_at=project.created_at,
            updated_at=project.updated_at,
            created_by=project.created_by,
            updated_by=project.updated_by,
            location=proj.location,
            area=proj.area,
            project_status=proj.project_status,
            custom_status=proj.custom_status,
            regulation_document=proj.regulation_document,
            cad_drafter_id=proj.cad_drafter_id,
            project_manager=proj.project_manager,
            org_id=proj.org_id,

             cad_drafter_name=(
            f"{(info.last_name or '')} "
            f"{(info.first_name[0] + '.' if info.first_name else '')}"
            f"{(info.fathers_name[0] + '.' if info.fathers_name else '')}".strip()
            if info else None
            ),
            cad_drafter_avatar=(f"{BASE_URL}{info.photo_url}" if info and info.photo_url else None)
        )
        for proj, project, info in results
    ]

# --- Получить проект по ID ---
@router.get("/{project_id}", response_model=ProjectRead, summary="Получить проект по ID")
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    project_info = db.query(ProjectInfo).filter_by(id=project_id).first()
    if not project_info:
        raise HTTPException(status_code=404, detail="Проект не найден")

    user_link = db.query(UserProject).filter_by(project_id=project_id, user_id=user_id).first()
    if not user_link and project_info.cad_drafter_id != user_id:
        raise HTTPException(status_code=403, detail="Нет доступа к проекту")

    return project_info

# --- Обновление проекта ---
@router.put("/{project_id}", response_model=ProjectRead, summary="Обновить проект")
def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    project_info = db.query(ProjectInfo).filter_by(id=project_id).first()
    if not project_info:
        raise HTTPException(status_code=404, detail="Проект не найден")

    for field, value in payload.dict(exclude_unset=True).items():
        setattr(project_info, field, value)

    project_info.updated_by = user_id
    project_info.updated_at = datetime.utcnow()

    if payload.name:
        project = db.query(Project).filter_by(id=project_id).first()
        if project:
            project.name = payload.name
            project.updated_by = user_id
            project.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(project_info)
    return project_info

# --- Удаление проекта ---
@router.delete("/{project_id}", summary="Удалить проект")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user_with_roles)
):
    project_info = db.query(ProjectInfo).filter_by(id=project_id).first()
    project = db.query(Project).filter_by(id=project_id).first()

    if not project_info or not project:
        raise HTTPException(status_code=404, detail="Проект не найден")

    is_creator = (project.created_by == user.id)
    is_org_admin = "admin" in user.role_names or "manager" in user.role_names
    project_org_id = project_info.org_id
    is_org_member = db.query(OrganizationMember).filter_by(
        org_id=project_org_id, user_id=user.id
    ).first()

    if not is_creator and not (is_org_admin and is_org_member):
        raise HTTPException(status_code=403, detail="Недостаточно прав для удаления проекта")

    db.delete(project_info)
    db.delete(project)
    db.commit()
    return {"detail": "Проект удалён"}

# --- Создание новой версии проекта ---
@router.post("/versions", response_model=ProjectVersionRead, summary="Создать версию проекта")
def create_project_version(
    payload: ProjectVersionCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    last = db.query(ProjectVersion).filter_by(project_id=payload.project_id)\
        .order_by(ProjectVersion.version.desc()).first()
    next_version = (last.version + 1) if last else 1

    version = ProjectVersion(
        project_id=payload.project_id,
        version=next_version,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(version)
    db.commit()
    db.refresh(version)
    return version

# --- Получение списка версий проекта ---
@router.get("/{project_id}/versions", response_model=List[ProjectVersionRead], summary="Версии проекта")
def get_project_versions(
    project_id: int,
    db: Session = Depends(get_db),
):
    return db.query(ProjectVersion).filter_by(project_id=project_id)\
        .order_by(ProjectVersion.version.desc()).all()
