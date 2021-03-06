"""empty message

Revision ID: ecee03a4d18
Revises: None
Create Date: 2014-10-27 14:16:35.830905

"""

# revision identifiers, used by Alembic.
revision = 'ecee03a4d18'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    ### end Alembic commands ###
