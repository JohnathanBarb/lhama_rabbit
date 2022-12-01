from pika import (
    ConnectionParameters,
    PlainCredentials,
    BlockingConnection,
    BasicProperties,
)

connection_parameters = ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=PlainCredentials(
        username="guest",
        password="guest",
    )
)
connection = BlockingConnection(connection_parameters)
channel = connection.channel()

channel.basic_publish(
    exchange="data_exchange",
    routing_key="",
    body=b"Hello World!",
    properties=BasicProperties(
        delivery_mode=2
    ),
)
