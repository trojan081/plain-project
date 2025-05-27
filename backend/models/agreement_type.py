from sqlalchemy import Column, String, Integer
from utils.ulid_generator import generate_ulid
from database import Base

class AgreementType(Base):
    __tablename__ = "agreement_types"

    id = Column(String, primary_key=True, default=lambda: generate_ulid())
    name = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"<AgreementType(id={self.id}, name={self.name!r})>"