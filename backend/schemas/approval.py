# backend/schemas/approval.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ApprovalBase(BaseModel):
    regulator_id: int
    project_id: int
    status: str
    comments: Optional[str] = None
    comments_file_url: Optional[str] = None

class ApprovalCreate(ApprovalBase):
    pass

class ApprovalRead(ApprovalBase):
    id: int
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # или from_attributes=True, если используете Pydantic v2
