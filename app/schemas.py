from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UnitEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    category: CategoryEnum
    description: str = Field(None, max_length=250)
    product_image: str = Field(None, max_length=2000)
    sku: str = Field(..., max_length=100)
    unit_of_measure: UnitEnum
    lead_time: int = Field(..., ge=1, le=999)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        orm_mode = True
