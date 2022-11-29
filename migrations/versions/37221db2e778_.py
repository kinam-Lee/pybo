"""empty message

Revision ID: 37221db2e778
Revises: 5e59d72c1023
Create Date: 2022-11-24 11:47:18.705884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37221db2e778'
down_revision = '5e59d72c1023'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])
        batch_op.create_unique_constraint(batch_op.f('uq_user_user_name'), ['user_name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_user_name'), type_='unique')
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    # ### end Alembic commands ###
