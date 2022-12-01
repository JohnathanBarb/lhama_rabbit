# RabbitMQ Producer and Consumer

## About
Some Python's scripts implementing a Producer and Consumer of using `pika` package
(a package that provides easily connection with AMQP protocol).

This project was made following a [Playlist](https://youtube.com/playlist?list=PLAgbpJQADBGLW5Q_OE86RzRb8HDvDzs-m)
from [ProgramadorLhama](https://www.youtube.com/@ProgramadorLhama)


## How to run
### Setting Environment Up
```sh
# Running RabbitMQ by Docker
docker run --rm -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

# Creating Python Environment and activating it
# preferentially using Python 3.10
python -m venv venv && source venv/bin/activate

# Installing Project Dependencies
pip install -r requirements.txt
```

### Running
In this project, we have:
* 2 Consumers:
  * Raw Consumer(`consumer_raw.py`)
  * Class Consumer(`consumer.py`)
* 2 Producers:
  * Raw Producer(`producer_raw.py`)
  * Class Producer(`producer.py`)

You can run it doing:
```shell
python consumer.py
```
