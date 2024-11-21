"""empty message

Revision ID: d787cf2f190a
Revises: 
Create Date: 2024-09-23 16:34:34.124374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd787cf2f190a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('first_name', sa.String(length=25), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('contact_number', sa.String(length=15), nullable=False),
    sa.Column('occupation', sa.String(length=50), nullable=False),
    sa.Column('gender', sa.String(length=6), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('postal_code', sa.String(length=4), nullable=False),
    sa.Column('role', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('active', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('id', sa.String(length=38), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('contact_number', name=op.f('uq_user_contact_number')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email')),
    sa.UniqueConstraint('id', name=op.f('uq_user_id'))
    )
    op.create_table('user_profile',
    sa.Column('bio', sa.String(length=200), nullable=True),
    sa.Column('avator', sa.String(length=250), nullable=True),
    sa.Column('user_id', sa.String(length=38), nullable=False),
    sa.Column('id', sa.String(length=38), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_profile_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_profile')),
    sa.UniqueConstraint('id', name=op.f('uq_user_profile_id'))
    )
    op.create_table('user_token',
    sa.Column('token', sa.String(length=72), nullable=False),
    sa.Column('expire', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('user_id', sa.String(length=38), nullable=False),
    sa.Column('id', sa.String(length=38), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_token_user_id_user'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_token')),
    sa.UniqueConstraint('id', name=op.f('uq_user_token_id')),
    sa.UniqueConstraint('token', name=op.f('uq_user_token_token'))
    )
    with op.batch_alter_table('user_token', schema=None) as batch_op:
        batch_op.create_index('ix_user_token_expire', ['expire'], unique=False)
        batch_op.create_index('ix_user_token_token', ['token'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_token', schema=None) as batch_op:
        batch_op.drop_index('ix_user_token_token')
        batch_op.drop_index('ix_user_token_expire')

    op.drop_table('user_token')
    op.drop_table('user_profile')
    op.drop_table('user')
    # ### end Alembic commands ###
