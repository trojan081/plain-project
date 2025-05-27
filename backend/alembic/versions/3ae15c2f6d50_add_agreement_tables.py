"""add agreement tables

Revision ID: 3ae15c2f6d50
Revises: 33a0a9f0ed79
Create Date: 2025-04-26 06:07:57.481887

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision: str = '3ae15c2f6d50'
down_revision: Union[str, None] = '33a0a9f0ed79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'agreement_types',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(length=50), nullable=False, unique=True),
    )
    # Сразу заполнить 4 типа
    op.bulk_insert(
        sa.table('agreement_types', sa.column('name', sa.String())),
        [
            {'name': 'offer'},
            {'name': 'advertisement'},
            {'name': 'personal_data'},
            {'name': 'policy'},
        ]
    )

    # 2) Таблица привязки пользователя к согласию
    op.create_table(
        'user_agreements',
        sa.Column('id',                sa.Integer(), primary_key=True),
        sa.Column('user_id',           sa.String(), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('agreement_type_id', sa.Integer(), sa.ForeignKey('agreement_types.id', ondelete='RESTRICT'), nullable=False),
        sa.Column('agreed',            sa.Boolean(), nullable=False),
        sa.Column('created_at',        sa.DateTime(), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at',        sa.DateTime(), nullable=True, onupdate=sa.func.now()),
        sa.Column('created_by',        sa.String(), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('updated_by',        sa.String(), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('user_agreements')
    op.drop_table('agreement_types')
