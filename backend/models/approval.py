from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Regulator(Base):
    __tablename__ = "regulators"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ApprovalStatus(Base):
    __tablename__ = "approval_status"

    id = Column(Integer, primary_key=True)
    status = Column(String, nullable=False)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Approval(Base):
    __tablename__ = "approvals"

    id = Column(Integer, primary_key=True)
    regulator_id = Column(Integer, ForeignKey("regulators.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    status = Column(String, nullable=False)
    comments = Column(String)
    comments_file_url = Column(String)
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    regulator = relationship("Regulator", backref="approvals")
    project = relationship("Project", backref="approvals")