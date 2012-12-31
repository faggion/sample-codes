# coding: utf-8
import os, logging, hashlib, hmac, urllib, urllib2, base64, urlparse, decimal, time
from flask import Flask,render_template,abort
from flask import make_response,request,url_for,redirect,Response,flash,session
from elixir import *
from sqlalchemy import create_engine,text

ro_engine = create_engine('mysql://root@localhost/test',
                          pool_recycle=30)
#ro_engine = create_engine('mysql://root@localhost/test')

rw_engine = create_engine('mysql://root@localhost/test',
                          pool_recycle=30)


setup_all()

app = Flask(__name__)
app.secret_key = 'tanarky'

@app.route('/ro')
def ro():
    sql = 'select name from users1 where id = :id;'
    id  = int(request.args.get('user_id', "1"))
    names = []
    for row in ro_engine.execute(text(sql), id=id):
        names.append(row[0])
    return ",".join(names)

@app.route('/rw')
def rw():
    sql = 'select name from users2 where id = :id;'
    id  = int(request.args.get('user_id', "5"))
    names = []
    for row in rw_engine.execute(text(sql), id=id):
        names.append(row[0])
    return ",".join(names)

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080, host='0.0.0.0')


