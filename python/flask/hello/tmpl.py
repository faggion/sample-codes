# coding: utf-8
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    v = {'name':u'あいうえお'}
    return render_template('test.html', M=v)
#    return render_template('test.html', name=u"あいうえお")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
