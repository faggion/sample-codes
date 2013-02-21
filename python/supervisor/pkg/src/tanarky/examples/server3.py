# coding: utf-8
import logging,os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    logging.error(os.environ.get('MYENV1'))
    return u"server3"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
