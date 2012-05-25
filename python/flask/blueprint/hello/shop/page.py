# -*- coding: utf-8 -*-

from flask import Blueprint

app = Blueprint('shop_page', __name__, url_prefix='/')

@app.route('/', methods=['GET'], strict_slashes=False)
def index():         
    return 'Shop Page'
