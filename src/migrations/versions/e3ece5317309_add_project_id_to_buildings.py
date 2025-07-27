"""add_project_id_to_buildings

Revision ID: e3ece5317309
Revises: 60e80c99a32c
Create Date: 2025-07-26 00:56:24.342538

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3ece5317309'
down_revision: Union[str, None] = '60e80c99a32c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('buildings', sa.Column('project_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_building_project', 'buildings', 'projects', ['project_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_building_project', 'buildings', type_='foreignkey')
    op.drop_column('buildings', 'project_id')
