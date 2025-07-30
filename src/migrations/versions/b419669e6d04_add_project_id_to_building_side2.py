"""add_project_id_to_building_side2

Revision ID: b419669e6d04
Revises: f215cab90af5
Create Date: 2025-07-30 10:23:40.076732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b419669e6d04'
down_revision: Union[str, None] = 'f215cab90af5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
