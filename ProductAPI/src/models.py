from pydantic import BaseModel
from typing import Optional


class Warehouse_location(BaseModel):
    country: str
    city: str = None


class Warehouse(BaseModel):
    id: str
    full_name: str = None
    location: Warehouse_location


class Product(BaseModel):
    id: int
    name: str
    quantityInStock: int
    quantityReserved: int


def generateMockProducts(x):
    warehouse_location = Warehouse_location(country = "Norway", city= "Oslo")
    warehouse = Warehouse(id='OS100', full_name="Oslo Terminal Vest", location=warehouse_location )

    result = []
    result.append(warehouse)

    from random import randint
    for x in range(1, 10):
        product = Product(id=x, name=f"item{x}", quantityInStock=randint(x, x*10), quantityReserved=randint(x, x*10))
        result.append(product)
    return result
