"""add_project_id_to_building_side1

Revision ID: f215cab90af5
Revises: a870d4f1a16d
Create Date: 2025-07-30 10:21:40.336182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f215cab90af5'
down_revision: Union[str, None] = 'a870d4f1a16d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
