from typing import Collection
from config import settings
from faunadb.client import FaunaClient
from faunadb import query as q

client = FaunaClient(secret=settings.db_secret)

indexes = client.query(q.paginate(q.indexes()))
print(indexes)  # Returns an array of all index created for the database.


class Order:
    def __init__(self) -> None:
        self.collection = q.collection("order")

    def get_order(self, id: int):
        return client.query(q.paginate(q.documents(q.collection('Order'))))

    def get_orders(self):

        return client.query(query.paginate(query.documents(self.collection)))

    def create_order(self, order_data):
        new_order = client.query(
            #TODO we might be able to use functions here?
            query.create(self.collection, order_data))

    def update_order(self, id: int, new_order_data):
        try:
            return client.query(
                query.update(query.ref(self.collection, id), new_order_data))
        except:
            return None  #TODO Create error handling

    def delete_order(self, id: int):
        try:
            return client.query(query.delete(query.ref(self.collection, id)))
        except:
            return None  #TODO Create error handling
