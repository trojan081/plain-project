from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class OrganizationCreate(BaseModel):
    name: str
    org_type: Optional[str] = None
    inn: Optional[str] = None
    location: Optional[str] = None
    email: Optional[str] = None

class OrganizationRead(OrganizationCreate):
    id: int

    class Config:
        from_attributes = True

class OrganizationMemberInvite(BaseModel):
    user_id: str

class OrganizationMemberRead(BaseModel):
    id: int
    org_id: int
    user_id: str
    employee_status_id: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
