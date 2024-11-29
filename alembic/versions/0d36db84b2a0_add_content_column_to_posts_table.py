"""add content column to posts table

Revision ID: 0d36db84b2a0
Revises: 11d31c3420e6
Create Date: 2024-11-29 17:02:50.392580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d36db84b2a0'
down_revision: Union[str, None] = '11d31c3420e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
