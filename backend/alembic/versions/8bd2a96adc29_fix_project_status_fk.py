"""fix project_status FK

Revision ID: 8bd2a96adc29
Revises: 2364521170fd
Create Date: 2025-04-30 15:15:10.422167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bd2a96adc29'
down_revision: Union[str, None] = '2364521170fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        constraint_name="project_info_project_status_fkey",
        table_name="project_info",  
        type_='foreignkey',
    )
    op.create_foreign_key(
        constraint_name='project_info_project_status_fkey', 
        source_table='project_info',
        referent_table='project_status',
        local_cols=['project_status'],
        remote_cols=['id']
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
