from typing import Annotated

from fastapi import APIRouter, Depends, status, Body, UploadFile, HTTPException

from src.depends import get_user
from src.models import Product, Category, Image, Unit
from src.schemas.product_schemas import (
    ProductCreateSchema,
    ProductDetailDisplaySchema, 
    ProductUpdateSchema, 
    UnitCreateSchema, 
    CategoryCreateSchema,
    CategoryDisplaySchema
    )

admin_router = APIRouter(tags=["admin"])

@admin_router.post(
    '/v1/admin/categories/', 
    response_model=CategoryDisplaySchema
)
async def create_cateogry(
    new_category: Annotated[
        CategoryCreateSchema, 
        Body()
    ] 
):
    """Создание категории"""
    try:
        category = await Category.create(
            **new_category.model_dump()
            )
    except ValueError as ex:
        raise HTTPException(detail=str(ex))
    return category

@admin_router.post('/v1/admin/units/')
async def create_unit(
    new_unit: Annotated[UnitCreateSchema, Body()]
):
    """Создание товара"""
    try:
        unit = await Unit.create(**new_unit.model_dump())
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return unit

@admin_router.post(
    '/v1/admin/products/', 
)
async def create_product(
    new_product: Annotated[
        ProductCreateSchema, 
        Body()
    ]
    ):
    """Создание товара"""
    try:
        product = await Product.create(**new_product.model_dump())
    except ValueError as ex:
        raise HTTPException(status_code=400, detail=str(ex))
    return product
    

@admin_router.get('/v1/admin/products/{product_id}')
async def delete_product():
    """Удаление товара"""
    pass

@admin_router.get('/v1/admin/products/{product_id}')
async def product():
    """Получение товара"""
    pass

@admin_router.get('/v1/admin/products/')
async def product():
    """Получение списка товаров"""
    pass

@admin_router.get('/v1/admin/products/')
async def product():
    """Получение списка товаров с фильтрацией"""
    pass

@admin_router.get('/v1/admin/products/')
async def product():
    """Изменение товара"""
    pass




