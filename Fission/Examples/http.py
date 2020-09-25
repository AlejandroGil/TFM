from flask import request

def main():
    try:
        myHeader = request.headers['test-header']
    except KeyError:
        return "Header 'test-header' not found"
    return "The header's value is '%s'" % myHeader
