#!/usr/bin/env python3

from flask import Flask
import tiltaccess
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return json.dumps(tiltaccess.get_data())

if __name__ == "__main__":
    app.run()
