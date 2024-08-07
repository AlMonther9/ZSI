"""complete sensors model

Revision ID: a4ec9d50c5bb
Revises: 7afea179e308
Create Date: 2024-03-17 23:39:43.261983

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a4ec9d50c5bb'
down_revision = '7afea179e308'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('air_quality', schema=None) as batch_op:
        batch_op.add_column(sa.Column('carbon_monoxide_ratio', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('temp', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('humidity', sa.Float(), nullable=False))
        batch_op.add_column(sa.Column('air_quality', sa.Float(), nullable=False))
        batch_op.alter_column('gaz',
               existing_type=mysql.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('real_time_coordinates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('google_maps', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('real_time_coordinates', schema=None) as batch_op:
        batch_op.drop_column('google_maps')

    with op.batch_alter_table('air_quality', schema=None) as batch_op:
        batch_op.alter_column('gaz',
               existing_type=sa.Integer(),
               type_=mysql.FLOAT(),
               existing_nullable=False)
        batch_op.drop_column('air_quality')
        batch_op.drop_column('humidity')
        batch_op.drop_column('temp')
        batch_op.drop_column('carbon_monoxide_ratio')

    # ### end Alembic commands ###
