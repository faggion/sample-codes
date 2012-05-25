# -*- coding: utf-8 -*-

from flask import Blueprint

app = Blueprint('tools_admin', __name__, url_prefix='/Tools/Admin')

@app.route('/', methods=['GET'], strict_slashes=False)
def index():         
    return 'Tools Admin Page'
