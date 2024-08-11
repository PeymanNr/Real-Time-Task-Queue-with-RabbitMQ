# Real-Time Task Queue with RabbitMQ

## Introduction 📄

This project demonstrates a real-time task queue system using RabbitMQ and Python. It includes a producer to send tasks to a queue and a consumer to process those tasks.

## Project Structure 📁
```python
real_time_task_queue/
├── task_producer.py 
├── task_consumer.py
├── connection.py
├── config.py
├── requirements.txt
├── README.md

```

## Setup 🛠️

1. **Install RabbitMQ** on your local machine or use Docker:
   ```python
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
   ```
Install Python dependencies:

```python
pip install -r requirements.txt
```
Configure RabbitMQ settings in config.py.

Running the Producer 🏭
Navigate to the producer directory and run:

```python
python task_producer.py
```
Running the Consumer 🏗️
Navigate to the consumer directory and run:

```python
python task_consumer.py
```

