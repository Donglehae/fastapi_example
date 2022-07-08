"""add content column to posts table

Revision ID: 67c18fcde2c8
Revises: 5466d6144870
Create Date: 2022-07-07 10:31:30.157877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67c18fcde2c8'
down_revision = '5466d6144870'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('content', sa.String(100), nullable=False)
                  )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
