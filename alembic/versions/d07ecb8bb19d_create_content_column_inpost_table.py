"""create content column inpost table

Revision ID: d07ecb8bb19d
Revises: ebd07749d67a
Create Date: 2024-09-07 23:53:14.276233

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd07ecb8bb19d'
down_revision: Union[str, None] = 'ebd07749d67a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
