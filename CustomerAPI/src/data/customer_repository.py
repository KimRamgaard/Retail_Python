#Import DB
from ..messages.message_publisher import CustomerPublisher

class CustomerRepo:
    #DB : CustomerDB
    customer_publisher = CustomerPublisher()

    def get_all_customers(self):
        # Call DB
        # Response = DB.FetchAll
        return "Not yet Implemented"

    def get_customer_by_id(self, customer_id):
        # Call DB
        return "Not yet Implemented"

    def update_customer(self, customer_json, customer_id):
        # Call DB
        return "Not yet Implemented"
    
    def create_customer(self, customer_json):
        # Call DB
        return "Not yet Implemented"
    
    def delete_costumer(self, customer_id):
        # Call DB
        return "Not yet Implemented"
    
    def check_credit_standing(self, order_json):
        # Call DB
        # This one could definitely use a function / index.
        # Check if CreditStanding is True/False
        
        # If True
        #Update customer 
        
        self.customer_publisher.order_accepted(order_json)
        # If False
        self.customer_publisher.order_rejected(order_json)
        return "Not yet Implemented"
    