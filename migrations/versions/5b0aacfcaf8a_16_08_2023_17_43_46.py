"""16.08.2023-17:43:46

Revision ID: 5b0aacfcaf8a
Revises: 3673fdc620ab
Create Date: 2023-08-16 17:43:47.440074

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b0aacfcaf8a'
down_revision = '3673fdc620ab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    # ### end Alembic commands ###
