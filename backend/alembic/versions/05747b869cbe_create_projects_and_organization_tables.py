"""create projects and organization tables

Revision ID: 05747b869cbe
Revises: b535dcc698e5
Create Date: 2025-04-28 16:20:03.173843

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05747b869cbe'
down_revision: Union[str, None] = 'b535dcc698e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    # Таблица ролей
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role', sa.String, nullable=False)
    )

    # Таблица статусов сотрудников
    op.create_table(
        'employee_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Список статусов для добавления
    statuses = [
        {'status': 'Active'},
        {'status': 'Vacation'},
        {'status': 'On Leave'},
        {'status': 'Probation'},
        {'status': 'Terminated'},
        {'status': 'Outsourcing'},
    ]

    # Вставка статусов в таблицу
    op.bulk_insert(
        sa.table('employee_status', sa.column('status', sa.String())),
        statuses
    )

    # Таблица организаций
    op.create_table(
        'organizations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('org_type', sa.String, nullable=True),
        sa.Column('inn', sa.String, nullable=True),
        sa.Column('location', sa.String, nullable=True),
        sa.Column('email', sa.String, nullable=True),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Члены организаций
    op.create_table(
        'organization_members',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('org_id', sa.Integer, sa.ForeignKey('organizations.id')),
        sa.Column('user_id', sa.String, sa.ForeignKey('users.id')),
        sa.Column('employee_status_id', sa.Integer, sa.ForeignKey('employee_status.id')),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Пользовательские роли
    op.create_table(
        'user_roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String, sa.ForeignKey('users.id')),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id')),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Проекты
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
    )

    # Статусы проектов
    op.create_table(
        'project_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
    )

    # Основная информация о проектах
    op.create_table(
        'project_info',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('org_id', sa.Integer, sa.ForeignKey('organizations.id')),
        sa.Column('cad_drafter_id', sa.String, sa.ForeignKey('users.id')),
        sa.Column('project_manager', sa.String, sa.ForeignKey('users.id')),
        sa.Column('project_status', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('area', sa.String, nullable=True),
        sa.Column('location', sa.String, nullable=True),
        sa.Column('regulation_document', sa.String, nullable=True),
        sa.Column('custom_status', sa.String, nullable=True),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Версии проектов
    op.create_table(
        'project_versions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('version', sa.Integer, autoincrement=True),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Пользовательские проекты (связка)
    op.create_table(
        'user_projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String, sa.ForeignKey('users.id')),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Регуляторы
    op.create_table(
        'regulators',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Статусы согласования
    op.create_table(
        'approval_status',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Одобрения
    op.create_table(
        'approvals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('regulator_id', sa.Integer, sa.ForeignKey('regulators.id')),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('status', sa.Integer, sa.ForeignKey('approval_status.id')),
        sa.Column('comments', sa.String, nullable=True),
        sa.Column('comments_file_url', sa.String, nullable=True),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Все конструкции дорог
    op.create_table(
        'all_road_constructions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.String, sa.ForeignKey('users.id')),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('organizations.id')),
        sa.Column('construction', sa.JSON, nullable=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Привязка конструкций к проектам
    op.create_table(
        'project_road_constructions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('construction_id', sa.Integer, sa.ForeignKey('all_road_constructions.id')),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('type_number', sa.String, nullable=True),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

    # Комментарии
    op.create_table(
        'comments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('text', sa.String, nullable=False),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id')),
        sa.Column('reply_to_id', sa.Integer, sa.ForeignKey('comments.id'), nullable=True),
        sa.Column('is_deleted', sa.Boolean, default=False),
        sa.Column('created_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('updated_by', sa.String, sa.ForeignKey('users.id')),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now())
    )

# def downgrade():
#     op.drop_table("project_info")
#     op.drop_table("projects")

