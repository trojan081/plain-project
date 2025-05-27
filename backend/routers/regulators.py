from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.approval import Regulator
from schemas.regulator import RegulatorCreate, RegulatorRead
from dependencies.auth import get_current_user
from typing import List

router = APIRouter(prefix="/regulator", tags=["regulator"])

@router.post("/", response_model=RegulatorRead)
def create_regulator(payload: RegulatorCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    regulator = Regulator(
        name=payload.name,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(regulator)
    db.commit()
    db.refresh(regulator)
    return regulator

@router.get("/", response_model=List[RegulatorRead])
def list_regulators(db: Session = Depends(get_db)):
    return db.query(Regulator).all()
