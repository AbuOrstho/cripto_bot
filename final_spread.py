import json
import time

start_time = time.time()
all_token = json.load(open('url_lib.json', 'r', encoding='UTF-8'))

# Цены из файлов от запросов к серверу
binance_tickers = json.load(open(r'Binance\response_all_tickers.json', 'r', encoding="UTF-8"))
bitmart_tickers = json.load(open(r'BitMart\response_all_tickers.json', 'r', encoding="UTF-8"))
bitfinex_tickers = json.load(open(r'Bitfinex\response_all_tickers.json', 'r', encoding="UTF-8"))
coinex_tickers = json.load(open(r'Coinex\response_all_tickers.json', 'r', encoding="UTF-8"))
huobi_tickers = json.load(open(r'Huobi\response_all_tickers.json', 'r', encoding="UTF-8"))["data"]
kucoin_tickers = json.load(open(r'KuCoin\response_all_tickers.json', 'r', encoding="UTF-8"))['data']['ticker']
lbank_tickers = json.load(open(r'LBank\response_all_tickers.json', 'r', encoding="UTF-8"))['data']
mexc_tickers = json.load(open(r'MEXC\response_all_tickers.json', 'r', encoding="UTF-8"))

def prices():

    all_prices = {}

    # bitfinex
    for i in bitfinex_tickers:
        token_name = f"{i[0].upper().replace('_', '')[1:]}T"
        if token_name in all_token["Binance"]["coin"]:
            if token_name in all_prices:
                all_prices[token_name].append(["Bitfinex", i[1]])
            else:
                all_prices[token_name] = [["Bitfinex", i[1]]]

    # binance_tickers
    for i in binance_tickers:
        token_name = f"{i['symbol'].upper().replace('_', '')}"
        if token_name in all_token["Binance"]["coin"]:
            if token_name in all_prices:
                all_prices[token_name].append(["Binance", i["price"]])
            else:
                all_prices[token_name] = [["Binance", i["price"]]]

    # bitmart_tickers
    for i in bitmart_tickers["data"]["tickers"]:
        token_name = f"{i['symbol'].upper().replace('_', '')}"
        if token_name in all_token["Binance"]["coin"]:
            if token_name in all_prices:
                all_prices[token_name].append(["Bitmart", i['last_price']])
            else:
                all_prices[token_name] = [["Bitmart", i['last_price']]]

    return all_prices

print(prices())