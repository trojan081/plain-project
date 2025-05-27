from sqlalchemy import Column, String, DateTime, func, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from utils.ulid_generator import generate_ulid
from utils.gdpr_mixin import PersonalDataMixin
from models.user_agreements import UserAgreement
from models.user_info       import UserInfo

class User(Base, PersonalDataMixin):
    __tablename__ = "users"
    __personal_data_fields__ = ["email"]

    id            = Column(String, primary_key=True, default=generate_ulid)
    email         = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at    = Column(DateTime, server_default=func.now())
    public_slug   = Column(String, unique=True, index=True, nullable=True)

    # вот здесь указываем единственный FK — user_id
    agreements = relationship(
        "UserAgreement",
        back_populates="user",
        foreign_keys=[UserAgreement.user_id]
    )

    # чтобы не было лишних автоматически созданных атрибутов,
    # мы явно прописываем обратные связи creator/updater:
    created_agreements = relationship(
        "UserAgreement",
        back_populates="creator",
        foreign_keys=[UserAgreement.created_by]
    )
    updated_agreements = relationship(
        "UserAgreement",
        back_populates="updater",
        foreign_keys=[UserAgreement.updated_by]
    )

    info = relationship(
        "UserInfo",
        uselist=False,
        back_populates="user",
        foreign_keys="[UserInfo.user_id]"
    )


class UserRole(Base):
    __tablename__ = "user_roles"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_by = Column(String, ForeignKey("users.id"))
    updated_by = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)