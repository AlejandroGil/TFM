#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import json
import time
import datetime
import random

from kafka import KafkaConsumer, KafkaProducer
KAFKA_ENDPOINT = "a1b822d05435611e9b6fb02bbb4726b9-1482861151.eu-west-1.elb.amazonaws.com:9092"
TOPIC_NAME = "test-topic"

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()
        
    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=KAFKA_ENDPOINT)

        while not self.stop_event.is_set():
            t = time.time()
            ts = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d_%H%M%S')
            payload = {}
            payload['msg'] = random.randint(1,100)
            payload['timestamp'] = ts
            json_data = json.dumps(payload)
            producer.send(TOPIC_NAME, json_data)
            time.sleep(1)

        producer.close()

class Consumer(multiprocessing.Process):
    def __init__(self):
        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()
        
    def stop(self):
        self.stop_event.set()
        
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=KAFKA_ENDPOINT,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000)
        consumer.subscribe([TOPIC_NAME])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()
        
        
def main():
    tasks = [
        Producer()
        #Consumer()
    ]

    for t in tasks:
        t.start()

    time.sleep(10)
    
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()
        
        
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()