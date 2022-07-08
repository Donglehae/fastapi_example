"""add last few columns to posts table

Revision ID: 96ff030c0834
Revises: 2d5f9d9396e2
Create Date: 2022-07-07 10:55:05.280532

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as sdm


# revision identifiers, used by Alembic.
revision = '96ff030c0834'
down_revision = '2d5f9d9396e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sdm.TINYINT(1, unsigned=True), server_default=sa.text('1'), nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
