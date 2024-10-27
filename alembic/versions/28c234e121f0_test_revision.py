"""test revision

Revision ID: 28c234e121f0
Revises: 
Create Date: 2024-10-27 15:46:27.076491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28c234e121f0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('original_price', sa.Double(), nullable=True),
    sa.Column('customer_rating', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Double(), nullable=True),
    sa.Column('product_tracking_url', sa.String(length=2500), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=False),
    sa.Column('added_by', sa.BigInteger(), nullable=True),
    sa.Column('product_source', sa.Integer(), nullable=True),
    sa.Column('short_description', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('brand_name', sa.String(length=255), nullable=True),
    sa.Column('standard_shipping_rate', sa.String(length=255), nullable=True),
    sa.Column('size', sa.String(length=255), nullable=True),
    sa.Column('color', sa.String(length=255), nullable=True),
    sa.Column('marketplace', sa.Integer(), nullable=True),
    sa.Column('model_number', sa.String(length=255), nullable=True),
    sa.Column('seller_info', sa.String(length=255), nullable=True),
    sa.Column('number_of_reviews', sa.Integer(), nullable=True),
    sa.Column('rhid', sa.String(length=255), nullable=True),
    sa.Column('bundle', sa.Boolean(), nullable=True),
    sa.Column('clearance', sa.Boolean(), nullable=True),
    sa.Column('preorder', sa.Boolean(), nullable=True),
    sa.Column('stock', sa.String(length=255), nullable=True),
    sa.Column('freight', sa.Boolean(), nullable=True),
    sa.Column('gender', sa.String(length=255), nullable=True),
    sa.Column('affiliate_add_to_cart_url', sa.String(length=2500), nullable=True),
    sa.Column('max_number_of_qty', sa.Integer(), nullable=True),
    sa.Column('offer_type', sa.Integer(), nullable=True),
    sa.Column('available_online', sa.Boolean(), nullable=True),
    sa.Column('e_delivery', sa.Boolean(), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('wm_product_id', sa.String(length=255), nullable=True),
    sa.Column('amazon_id', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['added_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=False)
    op.create_table('wishlists',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wishlists_id'), 'wishlists', ['id'], unique=False)
    op.create_table('product_images',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=True),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('thumbnail', sa.String(length=255), nullable=True),
    sa.Column('medium_image', sa.String(length=255), nullable=True),
    sa.Column('large_image', sa.String(length=255), nullable=True),
    sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_images_id'), 'product_images', ['id'], unique=False)
    op.create_table('wishlist_products',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('wishlist_id', sa.BigInteger(), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('note', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['wishlist_id'], ['wishlists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wishlist_products_id'), 'wishlist_products', ['id'], unique=False)
    op.create_index(op.f('ix_wishlist_products_product_id'), 'wishlist_products', ['product_id'], unique=False)
    op.create_index(op.f('ix_wishlist_products_wishlist_id'), 'wishlist_products', ['wishlist_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wishlist_products_wishlist_id'), table_name='wishlist_products')
    op.drop_index(op.f('ix_wishlist_products_product_id'), table_name='wishlist_products')
    op.drop_index(op.f('ix_wishlist_products_id'), table_name='wishlist_products')
    op.drop_table('wishlist_products')
    op.drop_index(op.f('ix_product_images_id'), table_name='product_images')
    op.drop_table('product_images')
    op.drop_index(op.f('ix_wishlists_id'), table_name='wishlists')
    op.drop_table('wishlists')
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
