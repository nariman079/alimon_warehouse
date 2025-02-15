"""empty message

Revision ID: 21d90b272c2a
Revises: 64379ab9d4e0
Create Date: 2025-01-20 11:28:11.218469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '21d90b272c2a'
down_revision: Union[str, None] = '64379ab9d4e0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('adjustment_lines', sa.Column('sku', sa.Integer(), nullable=False))
    op.add_column('adjustment_lines', sa.Column('quantity', sa.Integer(), nullable=False))
    op.drop_column('adjustment_lines', 'article')
    op.add_column('adjustments', sa.Column('notice', sa.String(), nullable=False))
    op.drop_column('adjustments', 'noticy')
    op.alter_column('images', 'alt',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('products', sa.Column('sku', sa.Integer(), nullable=False))
    op.add_column('products', sa.Column('barcode', sa.String(), nullable=True))
    op.add_column('products', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_products_category_id_categories'), 'products', 'categories', ['category_id'], ['id'])
    op.add_column('receipt_lines', sa.Column('sku', sa.Integer(), nullable=False))
    op.drop_column('receipt_lines', 'unit')
    op.drop_column('receipt_lines', 'artile')
    op.add_column('receipts', sa.Column('notice', sa.String(), nullable=False))
    op.alter_column('receipts', 'receipt_datetime',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
    op.add_column('write_down_lines', sa.Column('sku', sa.Integer(), nullable=False))
    op.drop_column('write_down_lines', 'artile')
    op.add_column('write_downs', sa.Column('notice', sa.String(), nullable=False))
    op.drop_column('write_downs', 'noticy')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('write_downs', sa.Column('noticy', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('write_downs', 'notice')
    op.add_column('write_down_lines', sa.Column('artile', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('write_down_lines', 'sku')
    op.alter_column('receipts', 'receipt_datetime',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
    op.drop_column('receipts', 'notice')
    op.add_column('receipt_lines', sa.Column('artile', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('receipt_lines', sa.Column('unit', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('receipt_lines', 'sku')
    op.drop_constraint(op.f('fk_products_category_id_categories'), 'products', type_='foreignkey')
    op.drop_column('products', 'category_id')
    op.drop_column('products', 'barcode')
    op.drop_column('products', 'sku')
    op.alter_column('images', 'alt',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('adjustments', sa.Column('noticy', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('adjustments', 'notice')
    op.add_column('adjustment_lines', sa.Column('article', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('adjustment_lines', 'quantity')
    op.drop_column('adjustment_lines', 'sku')
    # ### end Alembic commands ###
