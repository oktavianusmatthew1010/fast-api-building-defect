"""add_project_id_to_building_side1

Revision ID: fbecaf9817ba
Revises: 26eb1bc5e234
Create Date: 2025-07-30 10:40:53.806353

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbecaf9817ba'
down_revision: Union[str, None] = '26eb1bc5e234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
