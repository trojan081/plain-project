from pydantic import BaseModel

class InvitationCreate(BaseModel):
    email: str
    org_id: int
