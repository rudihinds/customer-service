"""Initial database structure

Revision ID: f70bb80ebb85
Revises:
Create Date: 2019-01-12 15:59:32.256921

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f70bb80ebb85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('customer_id',
                  sa.Integer,
                  primary_key=True,
                  autoincrement=True),
        sa.Column('first_name', sa.String(200)),
        sa.Column('surname', sa.String(200))
    )


def downgrade():
    op.drop_table('customers')
