"""add_project_id_to_building_side2

Revision ID: 26eb1bc5e234
Revises: af4c440968c9
Create Date: 2025-07-30 10:40:50.204522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26eb1bc5e234'
down_revision: Union[str, None] = 'af4c440968c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
