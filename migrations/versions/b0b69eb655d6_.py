"""empty message

Revision ID: b0b69eb655d6
Revises: 
Create Date: 2019-12-17 16:55:58.928501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0b69eb655d6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('motor_name', sa.String(), nullable=True),
    sa.Column('timestamp', sa.String(), nullable=True),
    sa.Column('transaction_id', sa.Integer(), nullable=True),
    sa.Column('machine', sa.String(), nullable=True),
    sa.Column('received', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###
