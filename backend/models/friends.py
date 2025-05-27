# 📄 backend/models/friends.py
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.sql import func
from database import Base

class Friend(Base):
    __tablename__ = "friends"

    user_id = Column(String, ForeignKey("users.id"), primary_key=True)
    friend_id = Column(String, ForeignKey("users.id"), primary_key=True)
    is_confirmed = Column(Boolean, default=False)
    is_blocked = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("user_id", "friend_id", name="uq_friend_pair"),
    )


# 📄 backend/models/project_visibility.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from database import Base

class ProjectVisibility(Base):
    __tablename__ = "project_visibility"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    visible_to_user_id = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
