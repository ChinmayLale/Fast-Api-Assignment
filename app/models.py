from sqlalchemy import Column, String, Integer, Enum, Text, BigInteger, DateTime
from app.database import Base
from datetime import datetime
from enum import Enum as PyEnum

class CategoryEnum(str, PyEnum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, PyEnum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class Product(Base):
    __tablename__ = "products"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String(250), nullable=True)
    product_image = Column(Text, nullable=True)
    sku = Column(String(100), nullable=False, unique=True)
    unit_of_measure = Column(Enum(UnitEnum), nullable=False)
    lead_time = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
