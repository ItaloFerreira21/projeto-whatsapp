"""Add User model

Revision ID: 1aaa8620f1bf
Revises: 
Create Date: 2025-01-11 18:30:50.617377

"""
from alembic import op
import sqlalchemy as sa


from alembic import op
import sqlalchemy as sa

# Revisão e IDs de downgrade
revision = '1aaa8620f1bf'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Criação da tabela user
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=80), nullable=False),
        sa.Column('password', sa.String(length=320), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username')
    )

def downgrade():
    # Remoção da tabela user
    op.drop_table('user')
