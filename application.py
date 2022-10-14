from flask import Flask, render_template, redirect, request, url_for, jsonify, Response
import pymongo
from pymongo import MongoClient
import certifi
import re

from ddtrace import tracer
from ddtrace import patch_all
patch_all()

application = Flask(__name__)
#CORS(application)

@tracer.wrap(name="index", service="csmail")
@application.route('/', methods=["GET"])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=5000)