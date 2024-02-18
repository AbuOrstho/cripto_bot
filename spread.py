import json

bitmark_prices = json.load(open(r'BitMart\response_1.json', 'r', encoding="UTF-8"))["data"]["tickers"]
coinex_prices = json.load(open(r'Coinex\response_1.json', 'r', encoding="UTF-8"))["data"]["ticker"]
huobi_prices = json.load(open(r'Huobi\response_1.json', 'r', encoding="UTF-8"))["data"]
lbank_prices = json.load(open(r'LBank\response_1.json', 'r', encoding="UTF-8"))["data"]
mexc_prices = json.load(open(r'MEXC\response_1.json', 'r', encoding="UTF-8"))["symbols"]


all_token = json.load(open('url_lib.json', 'r', encoding='UTF-8'))

all_key = all_token.keys()
print(all_key)
print("        Coinex    LBank    MEXC    BitMart")
for i in all_key:
    if all_token[i]['coin'] in bitmark_prices:
        print(all_token[i]['coin'])