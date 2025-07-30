"""add_project_id_to_building_side

Revision ID: a870d4f1a16d
Revises: 78c32b1de774
Create Date: 2025-07-30 10:19:12.931897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a870d4f1a16d'
down_revision: Union[str, None] = '78c32b1de774'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
