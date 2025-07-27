"""add_project_id_to_buildings3

Revision ID: d37dec50962f
Revises: 8f4356e82e0d
Create Date: 2025-07-26 11:30:22.716546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd37dec50962f'
down_revision: Union[str, None] = '8f4356e82e0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
