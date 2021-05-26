import json
import threading

import os
import pika

#Import customer repo here-

class CustomerListener(threading.Thread):
    #customer_repo = CustomerRepo()

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        if self.name =="create":
            self.order_created()
        if self.name =="reject":
            self.order_rejected()
        if self.name =="shipped":
            self.order_shipped()
        if self.name =="cancel":
            self.order_cancelled()
    
    
    def order_created(self):
        try:
            # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
            url = os.environ.get('CLOUDAMQP_URL',
                                 'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd')
            params = pika.URLParameters(url)
            params._socket_timeout = 5
            connection = pika.BlockingConnection(params)
            channel = connection.channel()  # start a channel
            channel.queue_declare(queue='create_order')  # Declare a queue

            def callback(ch, method, properties, body):
                body = body.decode('utf-8')
                body = json.loads(body)
                return self.customer_repo.check_credit_standing(body)

            channel.basic_consume('check_customer', callback, auto_ack=True)

            channel.start_consuming()

            connection.close()
        except Exception:
            print(Exception)

    def order_rejected(self):
        try:
            # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
            url = os.environ.get('CLOUDAMQP_URL',
                                 'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd')
            params = pika.URLParameters(url)
            params._socket_timeout = 5
            connection = pika.BlockingConnection(params)
            channel = connection.channel()  # start a channel
            channel.queue_declare(queue='create_order')  # Declare a queue

            def callback(ch, method, properties, body):
                body = body.decode('utf-8')
                body = json.loads(body)
                self.customer_repo.reject_order(body)

            channel.basic_consume('product_rejected', callback, auto_ack=True)

            channel.start_consuming()

            connection.close()
        except Exception:
            print(Exception)

    def order_canceled(self):
        try:
            # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
            url = os.environ.get('CLOUDAMQP_URL',
                                 'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd')
            params = pika.URLParameters(url)
            params._socket_timeout = 5
            connection = pika.BlockingConnection(params)
            channel = connection.channel()  # start a channel
            channel.queue_declare(queue='status_change')  # Declare a queue

            def callback(ch, method, properties, body):
                body = body.decode('utf-8')
                body = json.loads(body)
                self.customer_repo.status_change(body)

            channel.basic_consume('order_cancel', callback, auto_ack=True)

            channel.start_consuming()

            connection.close()
        except Exception:
            print(Exception)

    def order_shipped(self):
        try:
            # Access the CLOUDAMQP_URL environment variable and parse it (fallback to localhost)
            url = os.environ.get('CLOUDAMQP_URL',
                                 'amqp://mwdsvrdo:oJFb7X7G3odP7vrchz9UPCD3SDGAiABZ@cow.rmq2.cloudamqp.com/mwdsvrd')
            params = pika.URLParameters(url)
            params._socket_timeout = 5
            connection = pika.BlockingConnection(params)
            channel = connection.channel()  # start a channel
            channel.queue_declare(queue='status_change')  # Declare a queue

            def callback(ch, method, properties, body):
                body = body.decode('utf-8')
                body = json.loads(body)
                self.customer_repo.status_change(body)

            channel.basic_consume('order_ship', callback, auto_ack=True)

            channel.start_consuming()

            connection.close()
        except Exception:
            print(Exception)