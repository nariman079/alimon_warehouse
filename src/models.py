from datetime import date

from sqlalchemy import ForeignKey, Numeric, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.conf.database import Base


class Unit(Base):
    """
    Таблица "Изменерие"
    
    title (str): Наименование изменрения
    products (list[Product]): Продукты этого измерения
    """
    __tablename__ = 'units'
    title: Mapped[str] = mapped_column(nullable=False)
    products = relationship(
        'Product',
        back_populates='unit',
    )

class Product(Base):
    """
    Таблица "Продукт"

    sku (int): Артикул 
    title (str): Наименование 
    description (str): Описание 
    price (float): Стоимость 
    stock_quantity (int): Остаток на складе
    is_active (bool): Статус активный или не активый
    unit (Unit): Единица измерения
    images (list[Image]): Изображения продукта
    category (Category)): Категория продукта
    """
    __tablename__ = "products"

    sku: Mapped[int] = mapped_column(nullable=False)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)

    unit_id: Mapped[int] = mapped_column(ForeignKey('units.id'))
    unit = relationship(
        'Unit',
        back_populates='products',
        lazy='jointed'
    )
    images = relationship(
        "Image", 
        back_populates='product',
        cascade="all, delete-orphan",
        lazy="selectin"
    )
    category = relationship(
        "Category",
        back_populates='products',
        lazy='joined'
    )
    __table_args__ = (
        CheckConstraint(
            "stock_quantity >= 0",
            name="check_product_quantity"
        ),
        CheckConstraint(
            "price >= 0",
            name="check_product_price"
        ),
    )

    def __init__(self, **kwargs):
        if not self.id:
            # Объект новый 
            print("NEW OBJECT")

        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return (f"<Product(id={self.id}, "
                "title={self.title}, "
                "price={self.price}, "
                "stock_quantitiy={self.stock_quantitiy})>")

class Image(Base):
    """
    Таблица "Изображение"

    alt (str): На случай если изображение по ссылке не будет доступен
    url (str): Сслыка на изображение 
    """
    __tablename__ = "images"

    alt: Mapped[str] = mapped_column(nullable=True)
    url: Mapped[str] = mapped_column(nullable=False)
    
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product = relationship('Product', back_populates='images')

    def __repr__(self):
        return f"<Image(id={self.id}, alt={self.alt}, image={self.url})>"


class Category(Base):
    """
    Таблица "Категория"

    Аттрибуты:
    title (str): Название категории
    description (str): Описание категории
    products (list[Product]): Товары этой категории
    """
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    products = relationship("Product", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, title={self.title})>"


class WriteDown(Base):
    """
    Таблица "Списание"

    Аттрибуты:
    reason (str): Причина списания
    notice (str): Комментарий менеджера
    """
    __tablename__ = 'write_downs'

    reason: Mapped[str] = mapped_column(default='salvage', nullable=False)
    notice: Mapped[str] = mapped_column()

    write_down_lines = relationship(
        'WriteDownLine',
        back_populates='write_down',
        lazy='selectin'
    )

    __table_args__ = (
        CheckConstraint(
            reason.in_(['sale', 'defect', 'salvage']),
            name="check_write_down_reason"
        ),
    )

class WriteDownLine(Base):
    """
    Таблица "Позиция Списания"

    Аттрибуты:
    sku (int):  Артикул товара списания
    quantity (quantity): Колчество для списания
    """
    __tablename__ = 'write_down_lines'

    sku: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    write_down_id: Mapped[int] = mapped_column(ForeignKey('write_downs.id'))
    write_down = relationship(
        'WriteDown',
        back_populates='write_down_lines'
    )
    __table_args__ = (
        CheckConstraint(
            "quantity >= 0",
            name="check_write_down_line_quantity"
        ),
    )

class Receipt(Base):
    """
    Таблица "Поступление"

    Аттрибуты:
    receipt_datetime (date):  Дата поступления
    receipt_lines (list[ReceiptLine]): Товары для поступления
    notice (str): Комментарий менеджера 
    """
    __tablename__ = 'receipts'

    receipt_datetime: Mapped[date] = mapped_column(nullable=False)
    receipt_lines = relationship(
        'ReceiptLine',
        back_populates='receipt',
        lazy='selectin'
    )
    notice: Mapped[str] = mapped_column()
    

class ReceiptLine(Base):
    """
    Таблица "Позиция Поступления"

    Аттрибуты:
    title (str): Название товара
    sku (int): Артикул товара
    quantity (int): Количество поступившего товара
    price (float): Стоимость за единицу товара
    total_price (float): Полная стоимость, 
        вычисляется автоматически по формулк "total_price = price * quantity"
    
    """
    __tablename__ = 'receipt_lines'

    sku: Mapped[int] = mapped_column()

    title: Mapped[str] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2))
    total_price: Mapped[float] = mapped_column(Numeric(10,2))

    receipt_id: Mapped[int] = mapped_column(ForeignKey('receipts.id'))
    receipt = relationship(
        'Receipt',
        back_populates='receipt_lines',
        lazy='joined'
    )
    unit = relationship(
        'Unit',
        back_populates='receipt_lines',
        lazy='joined'
    )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.total_price = self.quantity * self.price

    __table_args__ = (
        CheckConstraint(
            "quantity >= 0",
            name="check_receipt_line_quantity"
        ),
    )

class Adjustment(Base):
    """
    Таблица "Корректировка"

    Аттрибуты:
    reason (str): Причина корректировки 
    notice (str): Комментарий менеджера 
    adjustment_lines (list[AdjustmentLine]): Товары для корректировки 
    """
    __tablename__ = 'adjustments'

    reason: Mapped[str] = mapped_column(nullable=False, default='invenotry_management')
    notice: Mapped[str] = mapped_column()

    adjustment_lines = relationship(
        'AdjustmentLine',
        back_populates='adjustment',
        lazy='selectin'
    )

    __table_args__ = (
        CheckConstraint(
            reason.in_(
                [
                    'invenotry_management',
                    'accounting_error', 
                    'system_error',
                    'salvage'
                ]
            ), name="check_adjustment_reason"
        ),
    )

class AdjustmentLine(Base):
    __tablename__ = 'adjustment_lines'

    sku: Mapped[int] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)

    adjustment_id: Mapped[int] = mapped_column(ForeignKey('adjustments.id'))
    adjustment = relationship(
        'Adjustment',
        back_populates='adjustment_lines'
    )
    __table_args__ =(
        CheckConstraint(
            "quantity >= 0",
            name="check_adujstment_quantity"
        ),
    )

