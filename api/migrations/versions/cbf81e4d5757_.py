"""empty message

Revision ID: cbf81e4d5757
Revises: 0476c76f9404
Create Date: 2019-03-20 11:47:10.205638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf81e4d5757'
down_revision = '0476c76f9404'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('csr', sa.Column('liaison_designate', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('csr', 'liaison_designate')
    # ### end Alembic commands ###
