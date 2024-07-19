import pika
import uuid
from utils.rabbit_connection import rabbit_connection


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf-8'))


connection = rabbit_connection
channel = connection.channel()

request_queue = 'request_queue'
reply_queue = 'reply_queue'

corr_id = str(uuid.uuid4())

channel.queue_declare(queue=reply_queue)

message = 'Hi Friend'
channel.basic_publish(
    exchange='', routing_key=request_queue,
    properties=pika.BasicProperties(
        reply_to=reply_queue,
        correlation_id=corr_id
    ),
    body=message.encode('utf-8'))
print(" [x] Sent %r" % message)


channel.basic_consume(queue=reply_queue, on_message_callback=callback)

print(' [*] Waiting for response. To exit, press CTRL+C')
channel.start_consuming()
