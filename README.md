# Real-Time Task Queue with RabbitMQ

## Introduction 📄

This project demonstrates a real-time task queue system using RabbitMQ and Python. It includes a producer to send tasks to a queue and a consumer to process those tasks.

## Project Structure 📁

real_time_task_queue/
├── producer/
│ ├── init.py
│ ├── task_producer.py
├── consumer/
│ ├── init.py
│ ├── task_consumer.py
├── utils/
│ ├── init.py
│ ├── rabbitmq_connection.py
├── config.py
├── requirements.txt
├── README.md

perl
Copy code

## Setup 🛠️

1. **Install RabbitMQ** on your local machine or use Docker:
   ```sh
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
Install Python dependencies:

sh
Copy code
pip install -r requirements.txt
Configure RabbitMQ settings in config.py.

Running the Producer 🏭
Navigate to the producer directory and run:

sh
Copy code
python task_producer.py
Running the Consumer 🏗️
Navigate to the consumer directory and run:

sh
Copy code
python task_consumer.py
Configuration ⚙️
Edit the config.py file to set your RabbitMQ connection parameters. Example:

python
Copy code
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_USER = 'guest'
RABBITMQ_PASSWORD = 'guest'
RABBITMQ_QUEUE = 'task_queue'
Example Usage 📝
Producer will send tasks to the queue.
Consumer will receive and process tasks from the queue.
Project Requirements 📋
Python 3.8+
RabbitMQ
License 📄
This project is licensed under the MIT License.

