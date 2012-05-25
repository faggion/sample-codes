# -*- coding: utf-8 -*-

from flask import Blueprint

app = Blueprint('shop_cart', __name__, url_prefix='/Cart')

@app.route('/', methods=['GET'], strict_slashes=False)
def index():         
    return 'Shop Cart Page'
