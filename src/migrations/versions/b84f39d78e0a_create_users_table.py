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
    op.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            login VARCHAR(50) NOT NULL,
            password TEXT NOT NULL
        );
    """)

def downgrade():
    op.execute("DROP TABLE users;")
