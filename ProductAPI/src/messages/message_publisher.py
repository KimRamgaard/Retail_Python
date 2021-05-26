import json

import os
import pika
from pika import URLParameters


class ProductPublisher:
    params: URLParameters

    def __init__(self):
        try:
            # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
            url = os.environ.get('CLOUDAMQP_URL',
                                 'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd')
            self.params = pika.URLParameters(url)
        except Exception:
            print(Exception)

    def order_accepted(self, order_json):
        connection = pika.BlockingConnection(self.params)
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='create_order')  # Declare a queue
        channel.basic_publish(exchange='',
                              routing_key='create_order',
                              body=json.dumps(order_json))

        print("order accepted'")
        connection.close()

    def order_rejected(self, order_json):
        connection = pika.BlockingConnection(self.params)
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='create_order')  # Declare a queue
        channel.basic_publish(exchange='',
                              routing_key='product_rejected',
                              body=json.dumps(order_json))

        print("order rejected")
        connection.close()