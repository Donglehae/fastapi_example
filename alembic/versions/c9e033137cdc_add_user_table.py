"""add user table

Revision ID: c9e033137cdc
Revises: 67c18fcde2c8
Create Date: 2022-07-07 10:36:13.211590

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as sdm


# revision identifiers, used by Alembic.
revision = 'c9e033137cdc'
down_revision = '67c18fcde2c8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sdm.INTEGER(unsigned=True), autoincrement=True, nullable=False),
                    sa.Column('email', sa.String(50), nullable=False),
                    sa.Column('password', sa.String(100), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
