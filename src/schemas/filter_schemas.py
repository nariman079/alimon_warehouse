from pydantic import BaseModel

class ProductFilter(BaseModel):
    category_id: int | None = None
    unit_id: int | None = None
    is_active: bool | None = None

