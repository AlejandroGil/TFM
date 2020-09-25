import flask
from flask import request
from flask import current_app
import redis
import time
import datetime

CLUSTER_IP = "100.64.216.240"

def main():
    current_app.logger.info("Running kafka_trigger function")
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%dT%H:%M:%S')

    r = redis.Redis(host=CLUSTER_IP, port=6379, db=0)
    r.set(st, request.get_json())
    resp = flask.Response("Inserted event {}:{}".format(st, request.get_json()))
    resp.status_code = 200
    return resp
