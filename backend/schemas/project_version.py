from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectVersionCreate(BaseModel):
    project_id: int

class ProjectVersionRead(BaseModel):
    id:         int
    project_id: int
    version:    int
    created_by: Optional[str]
    updated_by: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
