# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route('/')
def entry():
    return "Hello World!"
    # return app.send_static_file('home.html')


if __name__ == '__main__':
    app.run(debug=True)
