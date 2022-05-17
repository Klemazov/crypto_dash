from crypto_dash.model import db, CryptoName
from crypto_dash.model import CryptoName
from flask import Flask
from flask import render_template


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    @app.route('/')
    def hello():
        crypto = CryptoName.query.column_descriptions
        #TODO solve problem with db
        return str(crypto)
    return app
