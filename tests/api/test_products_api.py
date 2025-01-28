import pytest

from src.schemas.product_schemas import ProductCreateSchema

# @pytest.mark.asyncio
# async def test_create_product_not_category(client):
#     product_data = ProductCreateSchema(
#         sku="GO123",
#         title="Go champ",
#         price=120,
#         stock_quantity=20,
#         is_active=False,
#         unit_id=1,
#         category_id=1
#     )
#     response = client.post(
#         '/api/v1/products/',
#         data=product_data.json()
#     )

#     assert response.status_code == 400
#     assert response.json()['message'] == "Такой категории нет в системе"