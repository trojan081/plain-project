from database import Base
from sqlalchemy import Column, String, DateTime, JSON
from datetime import datetime

class PDataAction(Base):
    __tablename__ = "pdata_actions"

    id = Column(String, primary_key=True)
    event_type = Column(String, nullable=False)
    object_type = Column(String, nullable=False)
    object_id = Column(String, nullable=False)
    field = Column(String, nullable=True)
    old_value = Column(String, nullable=True)
    new_value = Column(String, nullable=True)
    performed_by = Column(String, nullable=True)
    performed_at = Column(DateTime, default=datetime.utcnow)