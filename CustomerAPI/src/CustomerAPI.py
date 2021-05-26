from fastapi import FastAPI
from typing import Optional
import schemas
import models

app = FastAPI()

mockOrders = schemas.generateTestCustomers(10)

@app.get("/")
async def root():

    return models.Customer().create_customer()


@app.get("/{customer_id}")
async def get_order_by_ID(order_id: int):
    return None


@app.post("/")
async def create_Order(customer: schemas.Customer):
    #this should save the order to DB
    return customer
