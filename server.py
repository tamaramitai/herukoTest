import os

from bottle import route, run

PORT = int(os.environ.get("PORT", 5000))


@route('/')
def home():
    return "Hello world!"


run(host='localhost', port=PORT)
