import requests

from crypto_dash.config import URL
from crypto_dash.model import db, CryptoName

res = requests.request(url=URL + '/ping', method='GET')

print(res.ok)


class CryptoCategories:
    def __init__(self, url: str, ):
        """
        get categories from gecko API
        :param url:
        """
        self.url_of_categories = url + '/coins/categories'

    def get_categories(self):
        return requests.request(url=self.url_of_categories, method='GET').json()


class CoinList:
    def __init__(self, url: str, ):
        self.url_of_list = url + '/coins/list'

    def get_coin_list(self):
        return requests.request(url=self.url_of_list, method='GET').json()


class CryptoSimplePrice:
    def __init__(self, url: str, ids, vs_currencies, ):
        self.url_of_simple_list = url + f'/simple/price?ids={ids}' \
                                        f'&vs_currencies={vs_currencies}' \
                                        f'&include_market_cap=true' \
                                        f'&include_24hr_vol=true' \
                                        '&include_24hr_change=true' \
                                        '&include_last_updated_at=true '

    def get_simple_price(self):
        return requests.request(url=self.url_of_simple_list, method='GET').json()


def save_crypto_list(crypto_id, symbol, name):
    id_exist = CryptoName.query.filter(CryptoName.crypto_id == crypto_id).count()
    if not id_exist:
        crypto_list = CryptoName(crypto_id=crypto_id, symbol=symbol, name=name)
        db.session.add(crypto_list)
        db.session.commit()


def save_each_from_crypto_list():
    list_ = CoinList(url=URL)
    for element in list_.get_coin_list():
        save_crypto_list(element.get('id'), element.get('symbol'), element.get('name'))


if __name__ == '__main__':
    # cat = CryptoCategories(URL)
    # print(cat.get_categories())
    # list_ = CryptoSimplePrice(url=URL, ids='bitcoin', vs_currencies='rub')
    # print(list_.get_simple_price())
    list_ = CoinList(url=URL)
    for element in list_.get_coin_list():
        save_crypto_list(element.get('id'), element.get('symbol'), element.get('name'))
    # print(list_.get_coin_list()[0:10])
    # save_crypto_list()
