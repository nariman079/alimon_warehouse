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
async def test_create_product(session):
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
async def test_create_product(session):
    unit_schema = UnitCreateSchema(
        title="шт"
    )
    category_schema = CategoryCreateSchema(
        title="new",
        description="it is new category"
    )

    unit = await Unit.create(**unit_schema.model_dump())
    category = await Category.create(**category_schema.model_dump())

    product_schema = ProductCreateSchema(
            sku="123",
            title="title",
            description="description",
            price=2200,
            stock_quantity=50,
            unit_id=unit.id,
            category_id=category.id
        )
    product = await Product.create(**product_schema.model_dump())
    
    assert unit.title == unit_schema.title
    assert product.unit.title == unit_schema.title
    assert product.category.title == category_schema.title



