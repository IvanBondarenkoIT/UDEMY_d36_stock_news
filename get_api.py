import requests
import config


def get_api(url, params):
    return requests.get(url, params=params).json()


def get_sales_api():
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': config.stock_name,
        'interval': '60min',
        'apikey': config.my_alphavantage_api,
    }
    return get_api(url=config.alphavantage_url, params=params)


def get_news_api():

    params = {
           'q': config.stock_name,
           'from': '2023-03-24',
           'sortBy': 'popularity',
           'apiKey': f"{config.my_news_api}"
        }
    return get_api(url=config.news_url, params=params)
