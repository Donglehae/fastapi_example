"""add foreign-key to posts table

Revision ID: 2d5f9d9396e2
Revises: c9e033137cdc
Create Date: 2022-07-07 10:47:56.314933

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy.dialects.mysql as sdm


# down, used by Alembic.
revision = '2d5f9d9396e2'
down_revision = 'c9e033137cdc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sdm.INTEGER(unsigned=True), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts", type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    pass
