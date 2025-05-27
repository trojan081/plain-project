from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectCreate(BaseModel):
    name:                str
    org_id:             Optional[int]
    project_manager:    Optional[str]
    project_status:     Optional[int]
    area:               Optional[str]
    location:           Optional[str]
    regulation_document: Optional[str]
    custom_status:      Optional[str]

class ProjectUpdate(BaseModel):
    name:                Optional[str]
    org_id:             Optional[int]
    project_manager:    Optional[str]
    project_status:     Optional[int]
    area:               Optional[str]
    location:           Optional[str]
    regulation_document: Optional[str]
    custom_status:      Optional[str]

class ProjectRead(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str

    location: Optional[str]
    area: Optional[str]
    project_status: Optional[int]
    custom_status: Optional[str]
    regulation_document: Optional[str]
    cad_drafter_id: Optional[str]
    project_manager: Optional[str]
    org_id: Optional[int]
    cad_drafter_name: Optional[str]
    cad_drafter_avatar: Optional[str]
    class Config:
        from_attributes = True

