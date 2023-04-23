import requests
import config


def get_sales_api():
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': 'IBM',
        'interval': '60min',
        'apikey': config.my_alphavantage_api,
    }
    # response.raise_for_status()
    return requests.get(url, params=params).json()


def get_news_api():
    url = 'https://newsapi.org/v2/everything'
    params = {
           'q': 'IBM',
           'from': '2023-03-23',
           'sortBy': 'popularity',
           'apiKey': f"{config.my_newsapi_api}"
        }

    return requests.get(url, params=params).json()
