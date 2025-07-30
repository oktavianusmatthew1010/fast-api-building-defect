"""add_project_id_to_buildings

Revision ID: 78c32b1de774
Revises: 363f7bb5b092
Create Date: 2025-07-30 10:12:07.305994

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78c32b1de774'
down_revision: Union[str, None] = '363f7bb5b092'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
