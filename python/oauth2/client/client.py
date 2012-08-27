import logging, ConfigParser, os
from flask import Flask, Response, request, flash, render_template, redirect, url_for, make_response, session
from functools import wraps
from oauth2 import Client

app = Flask(__name__)
app.secret_key = 'tanarkyclient'

KEY      = 'key1'
SECRET   = 'user1secret'
CALLBACK = 'http://localhost:8081/login'

client = Client(KEY,
                SECRET, 
                site='http://localhost:8080', 
                authorize_url='http://localhost:8080/authorize',
                token_url='http://localhost:8080/access_token')


@app.route('/')
def index():
    authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='user,public_repo')    
    return render_template('index.html', authorize_url=authorize_url)

# http://localhost/~satoshi.tanaka/oauth2/callback?code=d0429cdfc52701f150a1&state=
# http://localhost/~satoshi.tanaka/oauth2/callback?state=error
@app.route('/login')
def login():
    code  = request.args.get('code', '')
    state = request.args.get('state', '')

    if code != '' and state == '':
        # request to access_token
        access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, parse='query')
        logging.error(access_token.token)
        logging.error(access_token.client)
        logging.error(access_token.opts)
        logging.error(access_token.headers)
        return 'OK'
    else:
        authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='user,public_repo')
        return redirect(authorize_url)

#print 'get user info' 
#ret = access_token.get('/user')
##print ret.parsed
#
#print ret.status
#print ret.body
#print ret.response

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8081)

