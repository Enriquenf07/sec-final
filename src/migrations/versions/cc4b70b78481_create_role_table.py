"""create role table

Revision ID: cc4b70b78481
Revises: 4920754c58a4
Create Date: 2025-11-22 23:25:22.632788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cc4b70b78481'
down_revision: Union[str, None] = 'b84f39d78e0a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():
    op.create_table(
        'user_role',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role', sa.String(50), nullable=False),
        sa.Column('user', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
    )

def downgrade():
    op.drop_table('user_role')