import asyncio

import pytest
import pytest_asyncio

from sqlalchemy import exc

from src.models import Unit, Product, Category, Image
from src.conf.database import session_context
from src.conf.settings import async_session
from src.schemas.product_schemas import UnitCreateSchema, \
    ProductCreateSchema, \
    CategoryCreateSchema

@pytest_asyncio.fixture(scope="function", autouse=True)
async def session():
    async with async_session.begin() as session:
        session_context.set(session)
        yield 


@pytest.mark.asyncio
async def test_create_product():
    unit = await Unit.create(title="шт")
    category = await Category.create(
        title="Category1", 
        description='description'
    )
    product = await Product.create(
        sku="sku",
        title="title",
        description="description",
        price=2,
        stock_quantity=2,
        unit_id=unit.id,
        category_id=category.id
    )
    
    assert unit.title == "шт"
    assert product.unit.title == "шт"
    assert product.category.title == "Category1"


@pytest.mark.asyncio
async def test_get_product(session):
    pass



