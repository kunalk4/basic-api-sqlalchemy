"""empty message

Revision ID: 4cdce45670c1
Revises: 6921279d1dad
Create Date: 2023-01-16 20:35:49.371155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cdce45670c1'
down_revision = '6921279d1dad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('city')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('city', sa.VARCHAR(length=128), nullable=True))

    # ### end Alembic commands ###
