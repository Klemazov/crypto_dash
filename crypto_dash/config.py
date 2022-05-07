import os

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'crypto_dash.db')
URL = 'https://api.coingecko.com/api/v3'

