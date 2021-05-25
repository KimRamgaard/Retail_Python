from enum import Enum
from pydantic import BaseModel


class ProductOrder():
    def __init__(self, id, orderID, quantity) -> None:
        self.id = id
        self.orderID = orderID
        self.quantity = quantity


class Order():
    def __init__(self, id, customerID) -> None:
        self.id = id
        self.customerID = customerID
        self.products = []

    def addProductToOrder(self, product_order: ProductOrder):
        self.products.append(product_order)


def get_orders_by_id(orders: list[Order], id):
    orders_by_id = []
    for order in orders:
        if order.id == id:
            orders_by_id.append(order)
    return orders_by_id


def generateTestOrders(x):
    orders = []

    for x in range(1, 10):
        order = Order(x, x % 3 + 1)
        orders.append(order)
    return orders