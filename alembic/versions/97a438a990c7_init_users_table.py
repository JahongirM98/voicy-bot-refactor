"""init users table

Revision ID: 97a438a990c7
Revises: 
Create Date: 2025-06-11 06:45:03.226649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97a438a990c7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('social_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('registration_date', sa.DateTime(), nullable=True),
    sa.Column('taps', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
