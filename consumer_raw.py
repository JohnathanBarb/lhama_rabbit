from pika import ConnectionParameters, PlainCredentials, BlockingConnection


def callback_function(ch, method, properties, body):
    print(body)


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
channel.queue_declare(
    queue="data_queue",
    durable=True,
)

channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=callback_function,
)

print("Consumer ON!")
channel.start_consuming()
