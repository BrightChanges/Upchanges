"""shit the fuck

Revision ID: 71a8fc24db67
Revises: 094483b3354a
Create Date: 2020-04-03 15:22:32.541176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71a8fc24db67'
down_revision = '094483b3354a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('blog_image', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_post', 'blog_image')
    # ### end Alembic commands ###