from fastapi import FastAPI
from typing import Optional
import schemas
import models

app = FastAPI()

mockOrders = schemas.generateTestOrders(10)


@app.get("/")
async def root(customerID: Optional[int] = None):
    return mockOrders


@app.get("/{order_id}")
async def get_order_by_ID(order_id: int):
    return schemas.get_orders_by_id(mockOrders, order_id)


@app.post("/")
async def create_Order(order: schemas.Order):
    #this should save the order to DB
    return order


@app.post("/")
async def change_Order(order: schemas.Order):
    #this should save the order to DB
    return order
