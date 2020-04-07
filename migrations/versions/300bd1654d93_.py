"""empty message

Revision ID: 300bd1654d93
Revises: 2a14cd0324f0
Create Date: 2020-04-06 21:04:30.322975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '300bd1654d93'
down_revision = '2a14cd0324f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('Artist', 'seeking_talent')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'seeking_venue')
    # ### end Alembic commands ###
