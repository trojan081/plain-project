"""add public_slug to users

Revision ID: 9851ce15bdec
Revises: cb93e8fa51f4
Create Date: 2025-05-03 13:34:01.291569

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9851ce15bdec'
down_revision: Union[str, None] = 'cb93e8fa51f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('users', sa.Column('public_slug', sa.String(length=64), nullable=True))
    op.create_unique_constraint('uq_users_public_slug', 'users', ['public_slug'])

def downgrade():
    op.drop_constraint('uq_users_public_slug', 'users', type_='unique')
    op.drop_column('users', 'public_slug')
