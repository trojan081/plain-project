from pydantic import BaseModel
from datetime import datetime
from typing import Any, Optional

class ConstructionCreate(BaseModel):
    company_id: int
    name:       str
    construction: Any

class ConstructionRead(BaseModel):
    id:         int
    user_id:    str
    company_id: int
    name:       str
    construction: Any
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
