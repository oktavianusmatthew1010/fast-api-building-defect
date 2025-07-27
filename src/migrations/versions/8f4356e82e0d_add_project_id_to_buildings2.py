"""add_project_id_to_buildings2

Revision ID: 8f4356e82e0d
Revises: e3ece5317309
Create Date: 2025-07-26 01:02:22.029230

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f4356e82e0d'
down_revision: Union[str, None] = 'e3ece5317309'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
