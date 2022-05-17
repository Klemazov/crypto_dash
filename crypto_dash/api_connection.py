import requests
from config import URL
from urllib.parse import urlencode
class Ping():
    def __init__(self, URL) -> None:
        self.__url = URL
        self.res = requests.request(url=self.get_url + '/ping', method='GET')

    def __repr__(self) -> str:
        return f'API server status {self.res}'

    @property
    def get_url(self):
        return self.__url

    def status(self):
        return self.res.status_code


class Simple(Ping):
    def __init__(self, URL) -> None:
        super().__init__(URL)

    def get_simple_price(self,
                        ids,
                        vs_currencies,
                        include_market_cap = True, 
                        include_24hr_vol = True, 
                        include_24hr_change = True, 
                        include_last_updated_at = True):
                    
        url_dict = {'ids': ids,
                    'vs_currencies': vs_currencies, 
                    'include_market_cap': include_market_cap,
                    'include_24hr_vol': include_24hr_vol,
                    'include_24hr_change': include_24hr_change,
                    'include_last_updated_at': include_last_updated_at}

        api_path = urlencode(url_dict).lower()

        self.url = self.get_url + '/simple/price?' + api_path

        return requests.request(url=self.url, method='GET')


    def get_simple_token_price(self, 
                                ids, 
                                contract_addresses, 
                                vs_currencies, 
                                include_market_cap, 
                                include_24hr_vol, 
                                include_24hr_change, 
                                include_last_updated_at):
        pass

    def get_supported_vs_currencies(self):
        return requests.request(url=URL+'/simple/supported_vs_currencies')

class Coins(Ping):
    def __init__(self, URL) -> None:
        super().__init__(URL)
        self.url = self.get_url + '/coins/list'

    @property
    def get_coin_list(self, include_platform=False) :
         return requests.request(url=self.url, method='GET').json()

    def get_coin_markets(self, vs_currency, ids, category, order, per_page, page, sparkline, price_change_percentage):
        pass

    def get_coins_id(self, id, localization, tickers, market_data, community_data, developer_data, sparkline, ):
        pass

    def get_coins_id_tickers(self, id, exchange_ids, include_exchange_logo, page, order, depth):
        pass

    def get_coins_id_history(self, id, date, localization):
        pass

    def get_coins_id_market_chart(self, id, vs_currency, days, interval):
        pass

    def get_coins_id_marketchart_range(self, id, vs_currency, from_, to):
        pass

    def get_coins_id_ohlc(self, id, vs_currency, days):
        pass

class Contract(Ping):
    def __init__(self, URL) -> None:
        super().__init__(URL)

    def get_coin_id_contract_contractadress(self, id, contract_address):
        pass

    def get_coins_id_contract_contractadress_marketchart(self, id, contract_address, vs_currency, days):
        pass

    def get_coins_id_contract_contractadress_marketchart_range(self, id, contract_address, vs_currency, from_, to):
        pass

class AssetPlatforms(Ping):
    def __init__(self, URL) -> None:
        super().__init__(URL)

    def get_asset_platforms(self):
        pass

class Categories(Ping):
    def __init__(self, URL) -> None:
        super().__init__(URL)
    
    def get_coins_categories_list(self):
        pass

    def get_coins_categories(self):
        pass

##UTILS FUNCS
from dataclasses import dataclass

@dataclass
class CoinListModel:
    id: str
    symbol: str
    name: str


def to_database(data:list):
    for dict_element in data:
        print(dict_element.keys())
        break



if __name__ == '__main__':
    # check = Ping(URL)
    # print(check.status())
    # simple_list = Simple(URL)
    # print(simple_list.get_simple_price(ids='dogecoin', vs_currencies='usd').json())
    # list_of_coins = Coins(URL)
    # to_database(list_of_coins.get_coin_list)
    model = CoinListModel(id='id', symbol='symbol', name='name')
    print(model)