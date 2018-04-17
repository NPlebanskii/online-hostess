"""empty message

Revision ID: 0204235987b0
Revises: 321da92ea509
Create Date: 2018-04-12 16:00:22.497660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0204235987b0'
down_revision = '321da92ea509'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tables',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('establishment_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tables')
    # ### end Alembic commands ###