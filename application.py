# -*- coding: utf-8 -*-
from flask import Flask


application = Flask(__name__)


@application.route('/')
def entry():
    return application.send_static_file('home.html')
