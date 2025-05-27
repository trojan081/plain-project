from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base

class UserInfo(Base):
    __tablename__ = "user_info"
    __personal_data_fields__ = [
    "first_name",
    "middle_name",
    "last_name",
    "fathers_name",
    "phone",
    "photo_url",
    "position",
    ]

    id           = Column(Integer, primary_key=True, autoincrement=True)
    user_id      = Column(String, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    first_name   = Column(String, nullable=True)
    middle_name  = Column(String, nullable=True)
    last_name    = Column(String, nullable=True)
    fathers_name = Column(String, nullable=True)
    phone        = Column(String, nullable=True)
    photo_url    = Column(String, nullable=True)
    position     = Column(String, nullable=True)
    created_at   = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at   = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    created_by   = Column(String, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    updated_by   = Column(String, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="info", foreign_keys=[user_id])