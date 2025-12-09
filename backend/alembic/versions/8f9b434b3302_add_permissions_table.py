"""Add permissions table

Revision ID: 8f9b434b3302
Revises: aad62e20d1d7
Create Date: 2025-12-10 00:00:55.751167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '8f9b434b3302'
down_revision: Union[str, Sequence[str], None] = 'aad62e20d1d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create permissions table
    op.create_table(
        'permissions',
        sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column('key_name', sa.String(length=150), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('icon', sa.String(length=100), nullable=True),
        sa.Column('feature_id', sa.BigInteger(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['feature_id'], ['plan_features.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('key_name'),
    )
    op.create_index(op.f('ix_permissions_feature_id'), 'permissions', ['feature_id'], unique=False)
    op.create_index(op.f('ix_permissions_key_name'), 'permissions', ['key_name'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_permissions_key_name'), table_name='permissions')
    op.drop_index(op.f('ix_permissions_feature_id'), table_name='permissions')
    op.drop_table('permissions')