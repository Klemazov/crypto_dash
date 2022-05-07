from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CryptoName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crypto_id = db.Column(db.String, unique=True, nullable=False)
    symbol = db.Column(db.String)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<CryptoName {self.crypto_id}, {self.name}>'
