from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.projects import AllRoadConstruction, ProjectRoadConstruction
from schemas.construction import ConstructionCreate, ConstructionRead
from schemas.construction import ConstructionCreate, ConstructionRead
from dependencies.auth import get_current_user
from typing import List

router = APIRouter(prefix="/construction", tags=["construction"])

# === 📘 Блок 1: Каталог конструкций организации ===

@router.post("/", response_model=ConstructionRead)
def create_construction(
    payload: ConstructionCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    construction = AllRoadConstruction(
        user_id=user_id,
        company_id=payload.company_id,
        construction=payload.construction,
        name=payload.name,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(construction)
    db.commit()
    db.refresh(construction)
    return construction

@router.get("/", response_model=List[ConstructionRead])
def list_constructions(db: Session = Depends(get_db)):
    return db.query(AllRoadConstruction).all()


# === 📗 Блок 2: Привязка конструкций к проекту ===

@router.post("/project", response_model=ConstructionRead)
def add_project_construction(
    payload: ConstructionCreate,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user)
):
    record = RoadConstruction(
        construction_id=payload.construction_id,
        project_id=payload.project_id,
        type_number=payload.type_number,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

@router.get("/project/{project_id}", response_model=List[ConstructionRead])
def get_project_constructions(
    project_id: int,
    db: Session = Depends(get_db)
):
    return db.query(ProjectRoadConstruction).filter_by(project_id=project_id).all()
