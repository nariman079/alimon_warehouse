from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.depends import get_user

admin_router = APIRouter(tags=["admin"])


@admin_router.get("/products/")
async def get_full_cart(
    user: Annotated[get_user, Depends()]
):
    """Получение товаров"""
    pass

@admin_router.post(
    "/products/", 
    status_code=status.HTTP_201_CREATED
)
async def create_product(user: Annotated[get_user, Depends()]):
    """Создание товара"""
    pass

