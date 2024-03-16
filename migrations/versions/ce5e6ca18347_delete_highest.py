"""delete highest

Revision ID: ce5e6ca18347
Revises: c8b7ac53d521
Create Date: 2024-03-16 20:44:34.993894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce5e6ca18347'
down_revision = 'c8b7ac53d521'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('real_time_coordinates', schema=None) as batch_op:
        batch_op.drop_column('heightFromGround')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('real_time_coordinates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('heightFromGround', sa.FLOAT(), nullable=True))

    # ### end Alembic commands ###
