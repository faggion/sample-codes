# coding: utf-8
import logging
from flask import Flask, Response, request, flash, render_template, redirect, url_for
from flaskext.principal import Principal, Permission, RoleNeed
from flaskext.principal import Identity, identity_changed
from flaskext.principal import identity_loaded, RoleNeed, UserNeed

app = Flask(__name__)
app.secret_key = 'tanarky'

# load the extension
principals = Principal(app)

# Create a permission with a single Need, in this case a RoleNeed.
admin_permission = Permission(RoleNeed('admin'))

# protect a view with a principal for that need
@app.route('/admin')
@admin_permission.require()
def do_admin_index():
    return Response('Only if you are an admin')

# this time protect with a context manager
@app.route('/articles')
def do_articles():
    with admin_permission.require():
        return Response('Only if you are admin')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        identity_changed.send(app, identity=Identity(username))
        flash(u'login success')
        return redirect(url_for('login'))
    else:
        return render_template('form.html')

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    logging.debug('identity loaded')
    identity.provides.add(RoleNeed('admin'))

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    app.run(debug=True, port=8080)
