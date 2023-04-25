from get_api import *
from send_sms import send_sms


def main():
    data = get_sales_api()
    print(data)

    dates_set = sorted(list(set(i.split(' ')[0] for i in data['Time Series (60min)'])), reverse=True)

    yesterday = dates_set[0]
    before_yesterday = dates_set[1]
    print(before_yesterday, yesterday)

    yesterday_close_price = float(data['Time Series (60min)'].get(f'{yesterday} 20:00:00').get('4. close'))
    before_yesterday_close_price = float(data['Time Series (60min)'].get(f'{before_yesterday} 20:00:00').get('4. close'))
    print(yesterday_close_price, before_yesterday_close_price)

    price_difference = abs(yesterday_close_price - before_yesterday_close_price)
    if price_difference > yesterday_close_price * 0.01: # if price difference is greater than 1%
        print("Warning")
        news = get_news_api(yesterday)
        print(news)
        if news.get('status') == 'ok':
            for source in news.get('articles'):
                # print(f"{source.get('title')}\n{source.get('url')}")
                send_sms(sms_text=f"{source.get('title')}\n{source.get('url')}",
                         to_number=config.my_actual_phone_number)


if __name__ == '__main__':
    main()

