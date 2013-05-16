# coding: utf-8
import logging, traceback
from flask import Flask, make_response, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def form():
    return render_template('form.html')

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=5001)
