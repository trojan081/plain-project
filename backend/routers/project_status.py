from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.projects import ProjectStatus
from schemas.project_status import ProjectStatusRead
from typing import List

router = APIRouter(tags=["project_status"])

@router.get("/project_status/", response_model=List[ProjectStatusRead], summary="Получить все статусы проектов")
def get_project_status(db: Session = Depends(get_db)):
    return db.query(ProjectStatus).all()
