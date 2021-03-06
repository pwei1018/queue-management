"""empty message

Revision ID: 0476c76f9404
Revises: 4f3e25700ad5
Create Date: 2019-03-19 13:49:15.248331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0476c76f9404'
down_revision = 'c47b250bf785'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('booking', sa.Column('booking_contact_information', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('booking', 'booking_contact_information')
    # ### end Alembic commands ###
