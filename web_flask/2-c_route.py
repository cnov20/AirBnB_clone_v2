#!/usr/bin/python3

''' This module uses Flask to setup a Web Server Gateway Interface
    to a web application (HBNB) that enables the application to listen
    for requests to it / its web server, on a given port

    Defines routes and sends return message, indicating succesful connection
'''

from flask import Flask
app = Flask(__name__)
app.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    return 'C ' + text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
