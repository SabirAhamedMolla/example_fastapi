"""add content column to posts table

Revision ID: 557644f6f571
Revises: cb5f0a650ba4
Create Date: 2023-10-10 09:32:59.556878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '557644f6f571'
down_revision: Union[str, None] = 'cb5f0a650ba4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
