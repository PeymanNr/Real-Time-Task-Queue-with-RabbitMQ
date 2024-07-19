import pika
from utils.rabbit_connection import rabbit_connection

connection = rabbit_connection
channel = connection.channel()

queue_name = 'request_queue'


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode('utf-8'))
    response = "Hello back!"
    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties=pika.BasicProperties(
            correlation_id=properties.correlation_id
        ),
        body=response.encode('utf-8'))

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_declare(queue=queue_name)
channel.basic_consume(queue=queue_name, on_message_callback=callback)
print(' [*] Waiting for requests. To exit, press CTRL+C')
channel.start_consuming()

