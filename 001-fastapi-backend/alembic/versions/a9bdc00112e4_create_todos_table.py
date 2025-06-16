"""create todos table

Revision ID: a9bdc00112e4
Revises: ad1c380734f8
Create Date: 2025-06-16 15:55:44.060944

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9bdc00112e4'
down_revision: Union[str, None] = 'ad1c380734f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table todos(
        id bigserial primary key,
        name text,
        completed boolean not null default false
    )
    """)

def downgrade():
    op.execute("drop table todos;")