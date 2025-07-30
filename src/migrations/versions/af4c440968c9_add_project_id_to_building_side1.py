"""add_project_id_to_building_side1

Revision ID: af4c440968c9
Revises: b419669e6d04
Create Date: 2025-07-30 10:24:22.718359

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af4c440968c9'
down_revision: Union[str, None] = 'b419669e6d04'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
