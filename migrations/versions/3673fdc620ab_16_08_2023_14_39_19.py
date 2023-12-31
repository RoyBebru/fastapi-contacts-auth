"""16.08.2023-14:39:19

Revision ID: 3673fdc620ab
Revises: 2fcb4768247e
Create Date: 2023-08-16 14:39:20.143492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3673fdc620ab'
down_revision = '2fcb4768247e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    # ### end Alembic commands ###
