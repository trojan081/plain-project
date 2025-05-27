from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.approval import Approval
from schemas.approval import ApprovalCreate, ApprovalRead
from dependencies.auth import get_current_user
from typing import List

router = APIRouter(prefix="/approval", tags=["approval"])

@router.post("/", response_model=ApprovalRead)
def create_approval(payload: ApprovalCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    approval = Approval(
        regulator_id=payload.regulator_id,
        project_id=payload.project_id,
        status=payload.status,
        comments=payload.comments,
        comments_file_url=payload.comments_file_url,
        created_by=user_id,
        updated_by=user_id,
    )
    db.add(approval)
    db.commit()
    db.refresh(approval)
    return approval

@router.get("/by_project/{project_id}", response_model=List[ApprovalRead])
def get_project_approvals(project_id: int, db: Session = Depends(get_db)):
    return db.query(Approval).filter_by(project_id=project_id).all()
