"""friends and project visibility add

Revision ID: b61576bee8de
Revises: 9851ce15bdec
Create Date: 2025-05-03 14:19:21.631075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b61576bee8de'
down_revision: Union[str, None] = '9851ce15bdec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'friends',
        sa.Column('user_id', sa.String(), nullable=False),
        sa.Column('friend_id', sa.String(), nullable=False),
        sa.Column('is_confirmed', sa.Boolean(), server_default='false'),
        sa.Column('is_blocked', sa.Boolean(), server_default='false'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('NOW()')),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('user_id', 'friend_id'),
        sa.UniqueConstraint('user_id', 'friend_id', name='uq_friend_pair')
    )

    op.create_table(
        'project_visibility',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False),
        sa.Column('visible_to_user_id', sa.String(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('NOW()'))
    )

def downgrade():
    op.drop_table('project_visibility')
    op.drop_table('friends')
