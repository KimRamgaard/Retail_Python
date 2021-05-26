#Import DB

from messages.message_publisher import ProductPublisher

class ProductRepo:
    #DB
    product_publisher = ProductPublisher()
    
    def get_all_products(self):
        # Call DB
        return "Not yet Implemented"
    
    def get_product_by_id(self, product_id):
        # Call DB
        return "Not yet Implemented"
    
    def update_product(self, product_json, product_id):
        # Call DB
        return "Not yet Implemented"
    
    def create_product(self, product_json):
        # Call DB
        return "Not yet Implemented"
    
    def delete_product(self, product_id):
        # Call DB
        return "Not yet Implemented"
    
    def check_if_products_available(self, order_json):
        #For each item in order json, check if products have a large enough quantity. 
        # 
        # 
        # #####CREATE A FUNCTION FOR THIS IN DB
        #
        # 
        # 
        # Call DB
        return "Not yet Implemented"
    
    def accept_order(self, order_json):
        self.product_publisher.order_accepted(order_json)

    def reject_order(self, order_json):
        self.product_publisher.order_rejected(order_json)

    def ship_order(self, order_json):
        # Call DB to update product about the amount of items reserved
        return "Not yet Implemented"
    
    def cancel_order(self, order_json):
        # Call DB to update product about the amount of items reserved
        return "Not yet Implemented"