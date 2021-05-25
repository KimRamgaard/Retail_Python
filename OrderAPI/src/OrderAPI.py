from fastapi import FastAPI
from typing import Optional
import models

app = FastAPI()

mockOrders = models.generateTestOrders(10)


@app.get("/")
async def root(customerID: Optional[int] = None):
    return mockOrders


@app.get("/{order_id}")
async def get_order_by_ID(order_id: int):
    return models.get_orders_by_id(mockOrders, order_id)


@app.post("/")
async def create_Order(order: models.Order):
    #this should save the order to DB
    return order


@app.post("/")
async def change_Order(order: models.Order):
    #this should save the order to DB
    return order


'''
@app.get("/order/{order_status}")
async def get_orders_by_status(order_status: OrderStatus):
    if order_status == OrderStatus.new:
        return  {"orderstatus": "new"}
    if order_status == OrderStatus.pending:
        return  {"orderstatus": "pending"}
    if order_status == OrderStatus.verified:
        return  {"orderstatus": "verified"}


#how to handle optional parameters

from typing import Optional

@app.get("/products")
async def get_products(current_stock: int = None, warehouse: Optional[str] = None):
    return {"current stock": current_stock, "warehouse" : warehouse}
    '''