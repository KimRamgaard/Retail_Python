from fastapi import FastAPI
from typing import Optional
import models

app = FastAPI()

mockOrders = models.generateMockProducts(10)


@app.get("/")
async def root():
    return mockOrders


@app.get("/{productID}")
async def get_order_by_ID(productId):
    pass


@app.post("/product")
async def create_Order(Product: models.Product):
    #this should save the order to DB
    return Product


@app.put("/product/{id}")
async def change_Order(id: int, product: models.Product):
    #this should save the order to DB
    return product
