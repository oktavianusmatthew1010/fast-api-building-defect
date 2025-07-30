"""add_project_id_to_buildings4

Revision ID: e7d04e58cbef
Revises: d37dec50962f
Create Date: 2025-07-30 10:07:08.190972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e7d04e58cbef'
down_revision: Union[str, None] = 'd37dec50962f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
