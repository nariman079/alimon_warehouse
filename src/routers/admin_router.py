from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.depends import get_user

cart_router = APIRouter(tags=["admin"])


@cart_router.get("/products/")
async def get_full_cart(
    user: Annotated[get_user, Depends()]
):
    """Получение товаров"""
    pass

@cart_router.post(
    "/products/", 
    status_code=status.HTTP_201_CREATED
)
async def create_product(user: Annotated[get_user, Depends()]):
    """Создание товара"""
    pass

