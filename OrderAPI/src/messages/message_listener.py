import json
import threading

import os
import pika

#Import order repo here-

class OrderListener(threading.Thread):
    #order_repo = OrderRepo()
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        if self.name == 'create':
            self.order_created()
        if self.name == 'reject':
            self.order_rejected()

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
                self.order_repo.accept_order(body)

            channel.basic_consume('create_order', callback, auto_ack=True)

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
                self.order_repo.reject_order(body)

            channel.basic_consume('order_rejected', callback, auto_ack=True)

            channel.start_consuming()

            connection.close()
        except Exception:
            print(Exception)