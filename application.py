# -*- coding: utf-8 -*-
from flask import Flask


application = Flask(__name__)


@app.route('/')
def entry():
    return "Hello World!"
    # return app.send_static_file('home.html')
