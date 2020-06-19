"""added relationship between user and posts

Revision ID: 34a4c5a03bb4
Revises: e3d14967288f
Create Date: 2020-06-19 17:32:47.852219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a4c5a03bb4'
down_revision = 'e3d14967288f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'user', ['owner_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'owner_id')
    # ### end Alembic commands ###
