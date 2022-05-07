from crypto_dash import create_app
from crypto_dash.utils import save_each_from_crypto_list

app = create_app()

with app.app_context():
    save_each_from_crypto_list()