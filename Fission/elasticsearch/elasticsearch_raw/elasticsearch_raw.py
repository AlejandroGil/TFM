import flask
from flask import request
from flask import current_app
from elasticsearch import Elasticsearch

HOST = "100.96.3.2"
PORT = 9200
es = Elasticsearch([{'host':HOST, 'port':PORT}])

def main():
    current_app.logger.info("Running elasticsearch raw function")
    event = request.get_json()
    res = es.index(index='vehicles', doc_type='raw', body=event)
    current_app.logger.info("Event {} with id {}".format(res['result'], res["_id"]))
    resp = flask.Response("Event {} with id {}".format(res['result'], res["_id"]))
    resp.status_code = 200
    return resp
 