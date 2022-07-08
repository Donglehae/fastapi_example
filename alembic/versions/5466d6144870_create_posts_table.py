"""create posts table

Revision ID: 5466d6144870
Revises: 
Create Date: 2022-07-07 10:12:36.635434

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as sdm


# revision identifiers, used by Alembic.
revision = '5466d6144870'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sdm.INTEGER(unsigned=True), autoincrement=True, nullable=False),
                    sa.Column('title', sa.String(50), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
