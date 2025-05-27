# models/user_agreements.py
from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, func, Integer
from sqlalchemy.orm import relationship
from database import Base
from utils.ulid_generator import generate_ulid

class UserAgreement(Base):
    __tablename__ = "user_agreements"

    id                = Column(Integer, primary_key=True, autoincrement=True)
    user_id           = Column(String, ForeignKey("users.id"), nullable=False)
    agreement_type_id = Column(Integer, ForeignKey("agreement_types.id", ondelete="RESTRICT"), nullable=False)
    agreed            = Column(Boolean, nullable=False, default=False)
    created_at        = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at        = Column(DateTime, server_default=func.now(),
                                onupdate=func.now(), nullable=False)

    created_by        = Column(String, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    updated_by        = Column(String, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    # это — “владелец” соглашения
    user = relationship(
        "User",
        foreign_keys=[user_id],
        back_populates="agreements"
    )
    agreement_type = relationship("AgreementType", lazy="joined")
    # это — кто создал запись
    creator = relationship(
        "User",
        foreign_keys=[created_by],
        uselist=False,
        back_populates="created_agreements"
    )

    # это — кто обновил запись
    updater = relationship(
        "User",
        foreign_keys=[updated_by],
        uselist=False,
        back_populates="updated_agreements"
    )
