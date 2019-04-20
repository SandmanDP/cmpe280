# -*- coding: utf-8 -*-
from flask import Flask


application = Flask(__name__)


@application.route('/')
def entry():
    return application.send_static_file('home.html')


@application.route('/map')
def map():
    return application.send_static_file('map.html')


if __name__ == '__main__':
    application.run()
