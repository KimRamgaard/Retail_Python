import json

import os
import pika


class OrderPublisher:
    def create_order(self, order_json):
        # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
        url = os.environ.get(
            'CLOUDAMQP_URL',
            'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd'
        )
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='create_order')  # Declare a queue
        channel.basic_publish(exchange='',
                              routing_key='check_customer',
                              body=json.dumps(order_json))

        print('Sent customer validation')
        connection.close()

    def cancel_order(self, order_json):
        # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
        url = os.environ.get(
            'CLOUDAMQP_URL',
            'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd'
        )
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='change_status')  # Declare a queue
        channel.basic_publish(exchange='',
                              routing_key='order_cancel',
                              body=json.dumps(order_json))

        print('Sent customer validation')
        connection.close()

    def ship_order(self, order_json):
        # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
        url = os.environ.get(
            'CLOUDAMQP_URL',
            'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd'
        )
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()  # start a channel
        channel.queue_declare(queue='change_status')  # Declare a queue
        channel.basic_publish(exchange='',
                              routing_key='order_ship',
                              body=json.dumps(order_json))

        print('Sent customer validation')
        connection.close()