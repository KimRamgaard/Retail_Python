from fastapi import FastAPI
from typing import Optional
from data.order_repository import order_repository
import data.schemas as schemas

app = FastAPI()


@app.get("/")
async def root(customerID: Optional[int] = None):
    return order_repository.get_all_orders()


@app.get("/{order_id}")
async def get_order_by_ID(order_id: int):
    return order_repository.get_order_by_id(order_id)
    #return schemas.get_orders_by_id(mockOrders, order_id)


@app.post("/")
async def create_Order(order: schemas.Order):
    #this should save the order to DB
    return order_repository.create_order(order.json())


@app.post("/")
async def change_Order(order: schemas.Order):
    #this should save the order to DB
    return order
