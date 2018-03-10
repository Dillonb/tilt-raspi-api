#!/usr/bin/env python3

from flask import Flask
import tiltaccess

app = Flask(__name__)

@app.route('/')
def hello():
    return str(tiltaccess.get_data())
