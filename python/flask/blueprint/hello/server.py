# -*- coding: utf-8 -*-

from flask import Flask
from tools.admin   import app as admin
from tools.manager import app as manager
from shop.page     import app as shop_page
from shop.cart     import shop_cart

app = Flask(__name__)
app.secret_key = 'tanarky'

app.register_blueprint(admin)
app.register_blueprint(manager)
app.register_blueprint(shop_page)
app.register_blueprint(shop_cart, url_prefix='/cart')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
