# coding: utf-8
import os, sys, logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/update', methods=['POST'])
def update():
    logging.debug(request.form)
    return redirect(url_for('index'))

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True)
