"""add project_id to project_info

Revision ID: 2364521170fd
Revises: 5656e08744dc
Create Date: 2025-04-30 08:10:11.367391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2364521170fd'
down_revision: Union[str, None] = '5656e08744dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
        op.add_column(
        'project_info',
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False)
    )

def downgrade() -> None:
    """Downgrade schema."""
    pass
