#Import DB
from ..messages.message_publisher import OrderPublisher

class OrderRepo:
    #Import DB 
    order_publisher = OrderPublisher()
    
    def get_all_orders(self):
        # Call DB  - Has Index
        return "Not yet Implemented"
    
    def get_order_by_id(self, order_id):
        # Call DB  - Has Index
        return "Not yet Implemented"
    
    def update_order(self, order_json):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"
    
    def create_order(self, order_json):
        # Call DB - Probably need a proper fql query.
        
        #On Success
        self.order_publisher.create_order(order_json)
        return "Not yet Implemented"
    
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
        order = "not yet implemented" # Result from DB call
        # If order status == created
        
        self.order_publisher.cancel_order(order)
        return "Not yet Implemented"
    
    def ship_order(self, order_id):
        # Call DB - Could use function
        order = "Not yet implemented" #Result from DB#
        # If orderStatus === created 
        self.order_publisher.ship_order(order)
        return "Not yet Implemented"