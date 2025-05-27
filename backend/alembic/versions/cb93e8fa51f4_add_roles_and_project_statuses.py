"""add roles and project statuses

Revision ID: cb93e8fa51f4
Revises: 8bd2a96adc29
Create Date: 2025-05-03 12:24:44.484395

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb93e8fa51f4'
down_revision: Union[str, None] = '8bd2a96adc29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_unique_constraint("uq_roles_role", "roles", ["role"])

    op.execute("""
        INSERT INTO roles (role) VALUES
        ('admin'),
        ('manager'),
        ('user')
        ON CONFLICT (role) DO NOTHING;
    """)
    # Замените 'your_admin_user_id_here' на фактический ID администратора
    # или получите его из базы данных, если он уже существует

    # admin_user = db.query(User).filter(User.role == 'admin').first()
    # if admin_user:
    #     admin_id = admin_user.id
    # else:
    #     raise Exception("Admin user not found in the database.")
    op.create_unique_constraint("uq_statuses_status", "project_status", ["status"])
    admin_id = 'your_admin_user_id_here'

    op.execute(f"""
        INSERT INTO project_status (status, created_by, updated_by) VALUES
        ('В работе', '{admin_id}', '{admin_id}'),
        ('На согласовании', '{admin_id}', '{admin_id}'),
        ('В ожидании', '{admin_id}', '{admin_id}'),
        ('Внесение правок', '{admin_id}', '{admin_id}'),
        ('Завершён', '{admin_id}', '{admin_id}')
        ON CONFLICT (status) DO NOTHING;
    """)

def downgrade():
    op.execute("DELETE FROM roles WHERE role IN ('admin', 'manager', 'user');")
    op.execute("""
        DELETE FROM project_status WHERE status IN (
            'В работе',
            'На согласовании',
            'В ожидании',
            'Внесение правок',
            'Завершён'
        );
    """)