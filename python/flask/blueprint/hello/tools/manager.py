# -*- coding: utf-8 -*-

from flask import Blueprint

app = Blueprint('tools_manager', __name__, url_prefix='/Tools/Manager')

@app.route('/', methods=['GET'], strict_slashes=False)
def index():         
    return 'Tools Manager Page'
