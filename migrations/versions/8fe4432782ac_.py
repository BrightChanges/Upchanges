"""empty message

Revision ID: 8fe4432782ac
Revises: d0d040e970fc
Create Date: 2020-04-03 23:07:00.138242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe4432782ac'
down_revision = 'd0d040e970fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blog_post', 'blog_image')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog_post', sa.Column('blog_image', sa.VARCHAR(length=64), server_default=sa.text("'default_blog.jpg'"), nullable=False))
    # ### end Alembic commands ###
