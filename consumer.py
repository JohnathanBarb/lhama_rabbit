from pika import ConnectionParameters, PlainCredentials, BlockingConnection


class RabbitConsumer:
    def __init__(self, callback: callable) -> None:
        self.__host = "localhost"
        self.__port = 5672
        self.__username = "guest"
        self.__password = "guest"
        self.__queue = "data_queue"
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
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
            on_message_callback=self.__callback,
        )

        return channel

    def start(self):
        print("Listening RabbitMQ on Port 5672")
        self.__channel.start_consuming()


def minha_callback(ch, method, properties, body):
    print(body)


if __name__ == "__main__":
    consumer = RabbitConsumer(minha_callback)
    consumer.start()
