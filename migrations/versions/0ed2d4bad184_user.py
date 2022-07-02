"""user

Revision ID: 0ed2d4bad184
Revises: 71b3367e45e4
Create Date: 2022-07-01 11:23:51.423008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed2d4bad184'
down_revision = '71b3367e45e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_password', table_name='user')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_user_password', 'user', ['password'], unique=False)
    # ### end Alembic commands ###