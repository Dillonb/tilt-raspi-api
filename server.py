#!/usr/bin/env python3

from flask import Flask
from tiltblescan import extract_temp_and_sg

app = Flask(__name__)

@app.route('/')
def hello():
    return str(extract_temp_and_sg())
