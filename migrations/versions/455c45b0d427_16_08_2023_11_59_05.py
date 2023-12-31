"""16.08.2023-11:59:05

Revision ID: 455c45b0d427
Revises: ceac358cab0a
Create Date: 2023-08-16 11:59:05.667954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455c45b0d427'
down_revision = 'ceac358cab0a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50, collation='NOCASE'), nullable=True),
    sa.Column('email', sa.String(length=250, collation='NOCASE'), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('_contact_uc', 'contacts', type_='unique')
    op.create_unique_constraint('fullname_uc', 'contacts', ['name', 'lastname'])
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_constraint('fullname_uc', 'contacts', type_='unique')
    op.create_unique_constraint('_contact_uc', 'contacts', ['name', 'lastname'])
    op.drop_column('contacts', 'user_id')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
