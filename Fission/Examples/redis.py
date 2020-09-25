import redis
from flask import current_app

CLUSTER_IP = "100.67.255.222"

def main():
    r = redis.Redis(host=CLUSTER_IP, port=6379, db=0)
    current_app.logger.info("------ Inserting key in redis ------")
    r.set('key', 'fission')
    current_app.logger.info("------ Obtaining key in redis ------")
    current_app.logger.info("{}".format(r.get('key')))
    return "OK"
