# -*- coding: utf-8 -*-

from flask import Flask
from tools.admin   import app as admin
from tools.manager import app as manager
from shop.page     import app as shop_page
from shop.cart     import app as shop_cart

app = Flask(__name__)
app.register_blueprint(admin)
app.register_blueprint(manager)
app.register_blueprint(shop_page)
app.register_blueprint(shop_cart)

app.run()
