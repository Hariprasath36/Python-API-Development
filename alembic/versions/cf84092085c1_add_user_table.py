"""add user table

Revision ID: cf84092085c1
Revises: 0d36db84b2a0
Create Date: 2024-11-30 13:36:14.934960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cf84092085c1'
down_revision: Union[str, None] = '0d36db84b2a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False)),sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False),sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email')
    pass


def downgrade() -> None:
    pass
