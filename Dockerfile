FROM python:latest

LABEL authors="king"

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install -y tmux \
    && pip install -U pip && pip install -r requirements.txt

COPY . /code

EXPOSE 8000

CMD ["tmux", "new-session", "-d", "python task_consumer.py; tmux split-window -h 'python task_producer.py'; tmux -2 attach-session -d"]
