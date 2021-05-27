#Import DB
from ..messages.message_publisher import CustomerPublisher

class CustomerRepo:
    #DB : CustomerDB
    customer_publisher = CustomerPublisher()

    def get_all_customers(self):
        # Call DB - Has index
        return "Not yet Implemented"

    def get_customer_by_id(self, customer_id):
        # Call DB - Has index
        return "Not yet Implemented"

    def update_customer(self, customer_json, customer_id):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"
    
    def create_customer(self, customer_json):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"
    
    def delete_costumer(self, customer_id):
        # Call DB - Probably need a proper fql query.
        return "Not yet Implemented"
    
    # Gets called from the Listener
    def check_credit_standing(self, order_json):
        # Option 1
        # Use the get_customer_by_id  - with the customer Id from the order_json
        # Check validity then go to "if true - else"
        # 
        
        # Option 2
        # This one could definitely use a function / index.
        # Check if CreditStanding is True/False
        
        # If True
        #Update customer 
        
        self.customer_publisher.order_accepted(order_json)
        # If False
        self.customer_publisher.order_rejected(order_json)
        return "Not yet Implemented"
    