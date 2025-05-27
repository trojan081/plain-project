from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

    agreed_offer:    bool
    agreed_personal: bool
    agreed_policy:   bool

    agreed_advertisement: bool = False

class UserRead(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    password: str | None = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str