from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserInfoBase(BaseModel):
    first_name:   Optional[str]
    middle_name:  Optional[str]
    last_name:    Optional[str]
    fathers_name: Optional[str]
    phone:        Optional[str]
    photo_url:    Optional[str]
    position:     Optional[str]
    

class UserInfoUpdate(UserInfoBase):
    pass

class UserInfoRead(UserInfoBase):
    user_id: str
    photo_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True