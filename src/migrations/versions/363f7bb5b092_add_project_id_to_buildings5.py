"""add_project_id_to_buildings5

Revision ID: 363f7bb5b092
Revises: e7d04e58cbef
Create Date: 2025-07-30 10:08:13.648425

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '363f7bb5b092'
down_revision: Union[str, None] = 'e7d04e58cbef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
