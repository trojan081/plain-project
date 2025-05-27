from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectStatusRead(BaseModel):
    id:         int
    status:     str
    created_by: Optional[str]
    updated_by: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
