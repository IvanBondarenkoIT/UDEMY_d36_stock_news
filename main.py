from get_api import *
from send_sms import send_sms


def main():
    data = get_sales_api()
    news = get_news_api()
    print(news)
    print(data['Meta Data'])
    data = data['Time Series (60min)']
    for i in data:
        print(i, data[i])
        open_price = float(data[i]['1. open'])
        close_price = float(data[i]['4. close'])
        price_difference = abs(open_price - close_price)
        if price_difference > open_price * 0.01: # if price difference is greater than 1%
            print("Warning")


if __name__ == '__main__':
    main()

