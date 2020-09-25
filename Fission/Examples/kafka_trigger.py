import flask
from flask import request

def main():
    resp = flask.Response("{} (handled by fission)".format(request.get_json()))
    resp.status_code = 200
    return resp
