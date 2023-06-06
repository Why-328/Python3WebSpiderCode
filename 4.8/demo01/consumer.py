import pika

QUEUE_NAME = 'scrape'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)


def callback(ch, method, properties, body):
    print(f"Get {body}")


channel.basic_consume(queue=QUEUE_NAME, auto_ack=True, on_message_callback=callback)
channel.start_consuming()
