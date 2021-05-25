from fastapi import FastAPI
from typing import Optional
import models

app = FastAPI()

mockOrders = models.generateTestCustomers(10)


@app.get("/")
async def root():
    return mockOrders


@app.get("/{customer_id}")
async def get_order_by_ID(order_id: int):
    return None


@app.post("/")
async def create_Order(customer: models.Customer):
    #this should save the order to DB
    return customer
