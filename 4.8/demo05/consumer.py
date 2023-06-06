import pika
import requests
import pickle

MAX_PRIORITY = 100
QUEUE_NAME = 'scrape_queue'
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
session = requests.Session()


def scrape(request):
    try:
        response = session.send(request.prepare(), verify=False)
        print(f'success scraped {response.url}')
    except requests.RequestException as e:
        print(e)
        print(f'error occurrred when scraping {request.url}')


while True:
    method_frame, header, body = channel.basic_get(queue=QUEUE_NAME, auto_ack=True)
    if body:
        request = pickle.loads(body)
        print(f'Get {request}')
        scrape(request)
