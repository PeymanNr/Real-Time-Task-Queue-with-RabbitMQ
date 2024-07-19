from utils.rabbit_connection import rabbit_connection

connection = rabbit_connection
channel = connection.channel()

channel.queue_declare(queue='request_queue')


def on_reply_message_receive(ch, method, properties, body):
    print(f"Received request: {properties.correlation_id} ")
    channel.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        body=f" Reply to {properties.correlation_id}")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue='request_queue',
                      on_message_callback=on_reply_message_receive
                      )
print('Starting Server..! ')
channel.start_consuming()





print(' [*] Waiting for requests. To exit, press CTRL+C')

