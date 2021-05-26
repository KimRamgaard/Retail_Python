from typing import Collection
from config import settings
from faunadb.client import FaunaClient
from faunadb import query

client = FaunaClient(secret= settings.db_secret)

indexes = client.query(query.paginate(query.indexes()))
print(indexes) # Returns an array of all index created for the database.

class Product:
    
    def __init__(self) -> None:
        self.collection = query.collection("Product")

    def get_product(self, id: int):
        pass


    def get_products(self):

        return client.query(
                query.paginate(
                    query.documents(self.collection )
                    )
            )


    def create_product(self, productData):
        new_product = client.query(
            #TODO we might be able to use functions here?
            query.create(
                self.collection,
                productData
            )
        )


    def update_product(self, id: int, new_product_data):
        try:
            return client.query(
                query.update(
                    query.ref(self.collection, id),
                    new_product_data
                )
            )
        except:
            return None #TODO Create error handling


    def delete_product(self, id: int):
        try:
            return client.query(
                query.delete(
                    query.ref(self.collection, id)
                )
            )
        except:
            return None #TODO Create error handling