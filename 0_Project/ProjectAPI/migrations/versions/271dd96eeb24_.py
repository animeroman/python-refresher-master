"""empty message

Revision ID: 271dd96eeb24
Revises: 
Create Date: 2025-02-28 15:27:12.654538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '271dd96eeb24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
