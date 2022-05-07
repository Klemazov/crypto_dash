from crypto_dash.model import db, CryptoName
from crypto_dash.model import CryptoName
# def create_app():
#     db.init_app()

from flask import Flask
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    @app.route('/')
    def hello():
        crypto = CryptoName.query.all()
        #TODO solve problem with db
        print(crypto)
        return f'hi Hi {crypto[0]}'
    return app
