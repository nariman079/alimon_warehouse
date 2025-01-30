from pydantic import BaseModel

class ImageBaseSchema(BaseModel):
    alt: str | None = NameError
    ulr: str 

class CategoryBaseSchema(BaseModel):
    title: str 
    description: str

class ProductBaseSchema(BaseModel):
    sku: str
    barcode: str | None = None
    title: str 
    description: str 
    price: float
    stock_quantity: int
    is_active: bool = False
    unit_id: int
    category_id: int

class UnitBaseSchema(BaseModel):
    title: str

class ImageCreateSchema(ImageBaseSchema):
    pass

class ImageDisplaySchema(ImageBaseSchema):
    id: int

class UnitCreateSchema(UnitBaseSchema):
    pass

class UnitDisplaySchema(UnitBaseSchema):
    id: int

class CategoryCreateSchema(CategoryBaseSchema):
    pass

class CategoryDisplaySchema(CategoryBaseSchema):
    id: int

class ProductCreateSchema(ProductBaseSchema):
    pass

class ProductUpdateSchema(ProductBaseSchema):
    pass

class ProductDetailDisplaySchema(ProductBaseSchema):
    id: int
    category: CategoryDisplaySchema
    unit: UnitDisplaySchema
    images: list[ImageDisplaySchema]

class ProductListDisplaySchema(BaseModel):
    id: int
    sku: str
    title: str
    unit: UnitBaseSchema
    category: CategoryBaseSchema

