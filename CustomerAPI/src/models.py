from config import settings
from faunadb.client import FaunaClient
from faunadb import query

client = FaunaClient(secret= settings.db_secret)

indexes = client.query(query.paginate(query.indexes()))
print(indexes) # Returns an array of all index created for the database.

class Customer:
    
    def __init__(self) -> None:
        self.collection = query.collection("Customer")

    def get_customer(self, id: int):
        try:
            return client.query(
                    query.get(query.match(query.index('user_by_id'), id))
                )
        except:
            return None #TODO Create error handling


    def get_customers(self):

        return client.query(
                query.all(self.collection)
            )


    def create_customer(self, customerData):
        new_customer = client.query(
            #TODO we might be able to use functions here?
            query.create(
                self.collection,
                customerData
            )
        )


    def update_customer(self, id: int, newCustomerData):
        try:
            return client.query(
                query.update(
                    query.ref(self.collection, id),
                    newCustomerData
                )
            )
        except:
            return None #TODO Create error handling


    def delete_customer(self, id: int):
        try:
            return client.query(
                query.delete(
                    query.ref(self.collection, id)
                )
            )
        except:
            return None #TODO Create error handling