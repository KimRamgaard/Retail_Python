from pydantic import BaseModel

class Customer(BaseModel):
    id: int
    name: str
    #orders: Optional[list[Order]] = None


def generateTestCustomers(x):
    customers = []
    for i in range(1, x):
        customer = Customer(id=i, name=f"customer {i}")
        customers.append(customer)
    return customers
