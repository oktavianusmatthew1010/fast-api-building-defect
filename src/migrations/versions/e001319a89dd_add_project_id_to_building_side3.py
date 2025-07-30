"""add_project_id_to_building_side3

Revision ID: e001319a89dd
Revises: fbecaf9817ba
Create Date: 2025-07-30 11:00:14.719705

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e001319a89dd'
down_revision: Union[str, None] = 'fbecaf9817ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
