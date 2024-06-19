import pika
from config import *

credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
parameters_rabbit = pika.ConnectionParameters(
    host=rabbitmq_host, port=rabbitmq_port, credentials=credentials)
rabbit_connection = pika.BlockingConnection(parameters_rabbit)
