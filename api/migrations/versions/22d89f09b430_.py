"""empty message

Revision ID: 22d89f09b430
Revises: ad82a83aa9ed
Create Date: 2019-02-27 12:09:14.454199

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22d89f09b430'
down_revision = 'ad82a83aa9ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('csr', sa.Column('pesticide_designate', sa.Integer(), nullable=False))
    op.alter_column('exam', 'event_id',
               existing_type=mysql.VARCHAR(length=25),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('exam', 'event_id',
               existing_type=mysql.VARCHAR(length=25),
               nullable=False)
    op.drop_column('csr', 'pesticide_designate')
    # ### end Alembic commands ###
