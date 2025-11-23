"""create users table

Revision ID: b84f39d78e0a
Revises: 
Create Date: 2025-11-22 01:47:15.569430

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b84f39d78e0a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade():

    op.create_table(
        'company',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
    )

    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('login', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('password', sa.Text, nullable=False),
        sa.Column('company', sa.Integer, sa.ForeignKey('company.id'), nullable=False),
    )

def downgrade():
    op.drop_table('users')
    op.drop_table('company')
