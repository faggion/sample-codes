# coding: utf-8
from flask import Flask

from api.tag import app as api_tag
from api.content import app as api_content
from admin.editor import app as admin_editor

app = Flask(__name__)

app.secret_key = 'tanarky'

app.register_blueprint(api_tag)
app.register_blueprint(api_content)
app.register_blueprint(admin_editor)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
