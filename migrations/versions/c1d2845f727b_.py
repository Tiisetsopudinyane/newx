"""empty message

Revision ID: c1d2845f727b
Revises: d787cf2f190a
Create Date: 2024-09-23 17:32:45.898685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1d2845f727b'
down_revision = 'd787cf2f190a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('userId', sa.Integer(), autoincrement=True, nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('userId')

    # ### end Alembic commands ###