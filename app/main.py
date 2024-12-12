from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, models, schemas
from app.database import engine

# Create tables
models.Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

@app.get("/product/list", response_model=list[schemas.ProductResponse])
def list_products(page: int = 1, db: Session = Depends(get_db)):
    limit = 10
    offset = (page - 1) * limit
    return crud.get_products(db, skip=offset, limit=limit)

@app.get("/product/{pid}/info", response_model=schemas.ProductResponse)
def product_info(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/product/add", response_model=schemas.ProductResponse)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@app.put("/product/{pid}/update", response_model=schemas.ProductResponse)
def update_product(pid: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, pid, product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
