"""auto-vote

Revision ID: 5764ccf998c0
Revises: 96ff030c0834
Create Date: 2022-07-07 11:07:06.729085

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5764ccf998c0'
down_revision = '96ff030c0834'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('user_id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.Column('post_id', mysql.INTEGER(unsigned=True), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    op.alter_column('users', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=False,
               existing_server_default=sa.text('current_timestamp()'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=mysql.TIMESTAMP(),
               nullable=True,
               existing_server_default=sa.text('current_timestamp()'))
    op.drop_table('votes')
    # ### end Alembic commands ###
