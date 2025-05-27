from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class ProjectSummary(BaseModel):
    id: int
    name: str
    status: Optional[int]
    created_at: datetime
    location: Optional[str]


class UserProfileResponse(BaseModel):
    user_id: str
    public_slug: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    fathers_name: Optional[str]
    phone: Optional[str]
    position: Optional[str]
    photo_url: Optional[str]
    is_friend: bool
    projects: List[ProjectSummary]

    class Config:
        from_attributes = True
