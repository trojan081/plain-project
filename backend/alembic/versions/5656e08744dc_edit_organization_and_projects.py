"""Edit organization and projects

Revision ID: 5656e08744dc
Revises: 05747b869cbe
Create Date: 2025-04-29 08:46:54.320640
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '5656e08744dc'
down_revision: Union[str, None] = '05747b869cbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    conn = op.get_bind()
    insp = sa.inspect(conn)

    # === Обновления по Organizations ===
    if 'organizations' in insp.get_table_names():
        cols = [c['name'] for c in insp.get_columns('organizations')]
        if 'org_type' not in cols:
            op.add_column('organizations', sa.Column('org_type', sa.String(), nullable=True))
        if 'inn' not in cols:
            op.add_column('organizations', sa.Column('inn', sa.String(), nullable=True))
        if 'location' not in cols:
            op.add_column('organizations', sa.Column('location', sa.String(), nullable=True))
        if 'email' not in cols:
            op.add_column('organizations', sa.Column('email', sa.String(), nullable=True))

    # === Обновления по OrganizationMember ===
    if 'organization_members' in insp.get_table_names():
        cols = [c['name'] for c in insp.get_columns('organization_members')]
        if 'employee_status_id' not in cols:
            op.add_column(
                'organization_members',
                sa.Column('employee_status_id', sa.Integer(), sa.ForeignKey('employee_status.id'), nullable=True)
            )

    # === Таблица projects ===
    if 'projects' not in insp.get_table_names():
        op.create_table(
            'projects',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('name', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
            sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now()),
            sa.Column('created_by', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('updated_by', sa.String(), sa.ForeignKey('users.id')),
        )

    # === Таблица project_status ===
    if 'project_status' not in insp.get_table_names():
        op.create_table(
            'project_status',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('status', sa.String(), nullable=False),
            sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
            sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now()),
            sa.Column('created_by', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('updated_by', sa.String(), sa.ForeignKey('users.id')),
        )

    # === Таблица project_info ===
    if 'project_info' not in insp.get_table_names():
        op.create_table(
            'project_info',
            sa.Column('id', sa.Integer(), primary_key=True),
            sa.Column('project_id', sa.Integer(), sa.ForeignKey('projects.id'), nullable=False),
            sa.Column('org_id', sa.Integer(), sa.ForeignKey('organizations.id')),
            sa.Column('cad_drafter_id', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('project_manager', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('project_status', sa.Integer(), sa.ForeignKey('project_status.id')),
            sa.Column('area', sa.String(), nullable=True),
            sa.Column('location', sa.String(), nullable=True),
            sa.Column('regulation_document', sa.String(), nullable=True),
            sa.Column('custom_status', sa.String(), nullable=True),
            sa.Column('created_by', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('updated_by', sa.String(), sa.ForeignKey('users.id')),
            sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
            sa.Column('updated_at', sa.DateTime(), server_default=sa.func.now(), onupdate=sa.func.now()),
        )


def downgrade() -> None:
    conn = op.get_bind()
    insp = sa.inspect(conn)

    # === Откат project_info ===
    if 'project_info' in insp.get_table_names():
        op.drop_table('project_info')

    # === Откат project_status ===
    if 'project_status' in insp.get_table_names():
        op.drop_table('project_status')

    # === Откат projects ===
    if 'projects' in insp.get_table_names():
        op.drop_table('projects')

    # === Откат OrganizationMember ===
    if 'organization_members' in insp.get_table_names():
        cols = [c['name'] for c in insp.get_columns('organization_members')]
        if 'employee_status_id' in cols:
            op.drop_column('organization_members', 'employee_status_id')

    # === Откат Organizations ===
    if 'organizations' in insp.get_table_names():
        cols = [c['name'] for c in insp.get_columns('organizations')]
        for col in ('email', 'location', 'inn', 'org_type'):
            if col in cols:
                op.drop_column('organizations', col)
