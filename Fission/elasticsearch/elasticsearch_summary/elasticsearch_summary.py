import flask
import json
from flask import request
from flask import current_app
from elasticsearch import Elasticsearch

HOST = "100.64.216.240"
PORT = 9200
es = Elasticsearch([{'host':HOST, 'port':PORT}])

def main():
    current_app.logger.info("Running elasticsearch summary function")
    event = request.get_json()
    vin = event["vin"]

    query_search = json.dumps({
        "query": {
            "match": {
                "vin": vin
            }
        }
    })
    #Get vehicle existing summary
    response = es.search_exists(index="vehicles", doc_type="summary", body=query_search)
    
    #Check if vehicle exists
    if response["hits"]["total"]["value"] > 0:
        #If attribute does not exists in ES or is str or bool, it is inserted/overwritten
        if event["name"] not in response["hits"]["hits"][0]["_source"] or isinstance(event["value"], bool) or isinstance(event["value"], str):
            current_app.logger.info("Event field: {} is str, bool or non existing, inserting value: {}".format(event["name"], event["value"]))
            resp = flask.Response("Event field: {} is str, bool or non existing, inserting value: {}".format(event["name"], event["value"]))
            query_update = json.dumps({
                "doc" : {
                    event["name"] : event["value"]
                }
        else:
            updated_field = response["hits"]["hits"][0]["_source"][event["name"]] + event["value"]
            updated_field /= 2
            current_app.logger.info("Updating field mean {}:{}".format(event["name"], updated_field))
            resp = flask.Response("Updating field mean {}:{}".format(event["name"], updated_field))
            query_update = json.dumps({
                "doc" : {
                    event["name"] : updated_field
                }
        res = es.update(index='vehicles', doc_type='summary', id=response["hits"]["hits"][0]["_id"], body=query_update)
        current_app.logger.info("Event {} with id {}".format(res['result'], res["_id"]))
    else:
        query_insert = json.dumps({
            "timestamp_first_event" : event["timestamp"]
            "vin" : vin
            event["name"] : event["value"] 
            }
        }
        res = es.index(index='vehicles', doc_type='summary', body=event)
        current_app.logger.info("Event {} with id {}".format(res['result'], res["_id"]))
        resp = flask.Response("Event {} with id {}".format(res['result'], res["_id"]))
    
    resp.status_code = 200
    return resp
 