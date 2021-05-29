#FaunaDB
from typing import Collection
from config import settings
from faunadb.client import FaunaClient
from faunadb import query as q
#Messaging
from messages.message_publisher import OrderPublisher

#set connection to database
client = FaunaClient(secret=settings.db_secret)
indexes = client.query(q.paginate(q.indexes()))
# Returns an array of all index created for the database for logging
print(indexes)


class OrderRepo:
    def __init__(self) -> None:
        #constructor
        self.collection = q.collection("Order")
        self.order_publisher = OrderPublisher()

    def get_all_orders(self):
        return client.query(q.paginate(q.match(q.index("get_all_orders"))))

    def get_order_by_id(self, order_id):
        return client.query(
            q.get(q.match(q.index('get_order_by_id'), order_id)))

    def update_order(self, order_json):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"

    def create_order(self, order_json):
        # Call DB - Probably need a proper fql query.

        #On Success
        self.order_publisher.create_order(order_json)
        return client.query(q.create(self.collection, order_json))

    def delete_order(self, order_id):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"

    # All four below could be created through the use of a shared function with a FaunaDB Function.

    # Called By listener
    def reject_order(self, order_json):
        # Call DB - Could use function
        return "Not yet Implemented"

    # Called by listener
    def accept_order(self, order_json):
        # Call DB - Could use function
        return "Not yet Implemented"

    def cancel_order(self, order_id):
        # Call DB - Could use function
        order = "not yet implemented"  # Result from DB call
        # If order status == created

        self.order_publisher.cancel_order(order)
        return "Not yet Implemented"

    def ship_order(self, order_id):
        # Call DB - Could use function
        order = "Not yet implemented"  #Result from DB#
        # If orderStatus === created
        self.order_publisher.ship_order(order)
        return "Not yet Implemented"


order_repository = OrderRepo()