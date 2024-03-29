"""New Life 10

Revision ID: 5a7300e40934
Revises: 89976e876c2f
Create Date: 2020-07-14 23:15:24.534240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a7300e40934'
down_revision = '89976e876c2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CEO_password',
    sa.Column('password_id', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('context', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('password_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('CEO_password')
    # ### end Alembic commands ###
