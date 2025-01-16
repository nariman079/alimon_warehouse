from datetime import datetime

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship, Mapped, mapped_column

from src.conf.database import Base


class Unit(Base):
    __tablename__ = 'units'
    title: Mapped[str]
    products = relationship(
        'Product',
        back_populates='unit',
    )

class Product(Base):
    __tablename__ = "products"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10,2), nullable=False)
    stock_quantity: Mapped[int] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)

    unit_id: Mapped[int] = mapped_column(ForeignKey('units.id'))
    unit = relationship(
        'Unit',
        back_populates='products'
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
        lazy='selectin'
    )
    def __repr__(self) -> str:
        return (f"<Product(id={self.id}, "
                "title={self.title}, "
                "price={self.price}, "
                "stock_quantitiy={self.stock_quantitiy})>")

class Image(Base):
    __tablename__ = "images"

    alt: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'))
    product = relationship('Product', back_populates='images')

    def __repr__(self):
        return f"<Image(id={self.id}, alt={self.alt}, image={self.url})>"


class Category(Base):
    __tablename__ = "categories"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column()

    products = relationship("Product", back_populates="category")

    def __repr__(self) -> str:
        return f"<Category(id={self.id}, title={self.title})>"


class WriteDown(Base):
    __tablename__ = 'write_downs'

    reason: Mapped[str] = mapped_column()
    noticy: Mapped[str] = mapped_column()

    write_down_lines = relationship(
        'WriteDownLine',
        back_populates='write_down',
        lazy='selectin'
    )

class WriteDownLine(Base):
    __tablename__ = 'write_down_lines'

    artile: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()

    write_down_id: Mapped[int] = mapped_column(ForeignKey('write_downs.id'))
    write_down = relationship(
        'WriteDown',
        back_populates='write_down_lines'
    )

class Receipt(Base):
    __tablename__ = 'receipts'

    receipt_datetime: Mapped[datetime] = mapped_column()
    receipt_lines = relationship(
        'ReceiptLine',
        back_populates='receipt',
        lazy='selectin'
    )
    notice: Mapped[str] = mapped_column
    

class ReceiptLine(Base):
    __tablename__ = 'receipt_lines'

    title: Mapped[str] = mapped_column()
    artile: Mapped[int] = mapped_column()
    quantity: Mapped[int] = mapped_column()
    unit: Mapped[str] = mapped_column()
    price: Mapped[str] = mapped_column(Numeric(10,2))
    total_price: Mapped[float] = mapped_column(Numeric(10,2))
    
    receipt_id: Mapped[int] = mapped_column(ForeignKey('receipts.id'))
    receipt = relationship(
        'Receipt',
        back_populates='receipt_lines'
    )

class Adjustment(Base):
    __tablename__ = 'adjustments'

    reason: Mapped[str] = mapped_column()
    noticy: Mapped[str] = mapped_column()

    adjustment_lines = relationship(
        'AdjustmentLine',
        back_populates='adjustment',
        lazy='selectin'
    )

class AdjustmentLine(Base):
    __tablename__ = 'adjustment_lines'
    article: Mapped[int] = mapped_column()
    adjustment_id: Mapped[int] = mapped_column(ForeignKey('adjustments.id'))
    adjustment = relationship(
        'Adjustment',
        back_populates='adjustment_lines'
    )


