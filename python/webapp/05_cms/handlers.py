# coding: utf-8
from flask import Flask

from api.tag import app as api_tag
from api.content import app as api_content

app = Flask(__name__)

app.secret_key = 'tanarky'
app.register_blueprint(api_tag)
app.register_blueprint(api_content)

#app.register_blueprint(manager)
#app.register_blueprint(shop_page)
#app.register_blueprint(shop_cart, url_prefix='/cart')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
