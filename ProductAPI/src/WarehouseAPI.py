from fastapi import FastAPI
from typing import Optional
import schemas

app = FastAPI()

mockOrders = schemas.generateMockProducts(10)


@app.get("/")
async def root():
    return mockOrders


@app.get("/{productID}")
async def get_order_by_ID(productId):
    pass


@app.post("/product")
async def create_Order(Product: schemas.Product):
    #this should save the order to DB
    return Product


@app.put("/product/{id}")
async def change_Order(id: int, product: schemas.Product):
    #this should save the order to DB
    return product
