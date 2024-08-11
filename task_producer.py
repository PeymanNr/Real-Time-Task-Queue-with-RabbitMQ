import pika
import uuid
from connection import rabbit_connection


connection = rabbit_connection
channel = connection.channel()

reply_queue = channel.queue_declare(queue='', exclusive=True)


def on_reply_message_receive(ch, method, properties, body):
    print(f'reply received: {body}')


channel.basic_consume(
    queue=reply_queue.method.queue,
    auto_ack=True, on_message_callback=on_reply_message_receive
)

channel.queue_declare(queue='request_queue')
corr_id = str(uuid.uuid4())
print(f'Sending Request: {corr_id}')


channel.basic_publish(
    exchange='', routing_key='request_queue',
    properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=corr_id
    ),
    body='Can i request a reply')


print('starting Client ...')
channel.start_consuming()
