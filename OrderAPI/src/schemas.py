from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id: int
    orderID: int
    quantity: int


class Order(BaseModel):
    id: int
    CustomerId: int
    products: Optional[list[Product]] = None


def generateTestOrders(x):
    orders = []

    for x in range(1, 10):
        order = Order(id=x, CustomerId=x % 3 + 1)
        orders.append(order)
    return orders
