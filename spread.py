import json
import time
from collections import Counter
import time

start_time = time.time()
all_token = json.load(open('url_lib.json', 'r', encoding='UTF-8'))

# Цены из файлов от запросов к серверу
binance_tickers = json.load(open(r'Binance\response_all_tickers.json', 'r', encoding="UTF-8"))
bitmart_tickers = json.load(open(r'BitMart\response_all_tickers.json', 'r', encoding="UTF-8"))
coinex_tickers = json.load(open(r'Coinex\response_all_tickers.json', 'r', encoding="UTF-8"))
huobi_tickers = json.load(open(r'Huobi\response_all_tickers.json', 'r', encoding="UTF-8"))["data"]
kucoin_tickers = json.load(open(r'KuCoin\response_all_tickers.json', 'r', encoding="UTF-8"))['data']['ticker']
lbank_tickers = json.load(open(r'LBank\response_all_tickers.json', 'r', encoding="UTF-8"))['data']
mexc_tickers = json.load(open(r'MEXC\response_all_tickers.json', 'r', encoding="UTF-8"))


# # Количество монет на каждой бирже которые есть в топ 200
# print("Coinex", len(all_token["Coinex"]["coin"]))
# print("LBank", len(all_token["LBank"]["coin"]))
# print("MEXC", len(all_token["MEXC"]["coin"]))
# print("BitMart", len(all_token["BitMart"]["coin"]))
# print("Huobi", len(all_token["Huobi"]["coin"]))
# print("Binance", len(all_token["Binance"]["coin"]))
# print("KuCoin", len(all_token["KuCoin"]["coin"]))


# Файл со всеми коинами на каждой бирже
all_token = json.load(open('url_lib.json', 'r', encoding='UTF-8'))  # Полный json файл


# Списки для сохранения всех измененных данных
coinex_list = []
lbank_list = []
mexc_list = []
bitmart_list = []
huobi_list = []
binance_list = []
kucoin_list = []


# Перебор циклами каждой пары чтобы сделать их одинаковыми
for i in all_token["Coinex"]["coin"]:
    coinex_list.append(i.upper().replace('_', ''))
for i in all_token["LBank"]["coin"]:
    lbank_list.append(i.upper().replace('_', ''))
for i in all_token["MEXC"]["coin"]:
    mexc_list.append(i.upper().replace('_', ''))
for i in all_token["BitMart"]["coin"]:
    bitmart_list.append(i.upper().replace('_', ''))
for i in all_token["Huobi"]["coin"]:
    huobi_list.append(i.upper().replace('_', ''))
for i in all_token["Binance"]["coin"]:
    binance_list.append(i.upper().replace('_', ''))
for i in all_token["KuCoin"]["coin"]:
    kucoin_list.append(i.upper().replace('_', ''))


# Соберем все списки в один для анализа
all_lists = coinex_list + lbank_list + mexc_list + bitmart_list + huobi_list + binance_list + kucoin_list

# Подсчитаем, сколько раз каждый элемент встречается в объединенном списке
counter = Counter(all_lists)

# Найдем элементы, встречающиеся в 2, 3 и 4 списках
two_lists = [item for item, count in counter.items() if count == 2]
three_lists = [item for item, count in counter.items() if count == 3]
four_lists = [item for item, count in counter.items() if count == 4]
five_lists = [item for item, count in counter.items() if count == 7]


def prices():
    # Инициализируем словарь для хранения результатов
    coins_prices = {}

    for i in five_lists:
        # Для каждой монеты создаем словарь с ценами на разных биржах
        coins_prices[i] = {}

        for bp in bitmart_tickers["data"]["tickers"]:
            bitmart_coin = bp["symbol"].replace("_", "").upper()
            if bitmart_coin == i:
                coins_prices[i]["Bitmark"] = float(bp["last_price"])

        for cp in coinex_tickers:
            coinex_coin = cp.replace("_", "").upper()
            if coinex_coin == i:
                coins_prices[i]["Coinex"] = float(coinex_prices[cp]['last'])

        for hp in huobi_tickers:
            huobi_coin = hp["symbol"].replace("_", "").upper()
            if huobi_coin == i:
                coins_prices[i]["Huobi"] = float(hp["close"])

        for lp in lbank_tickers:
            lbank_coin = lp['symbol'].replace("_", "").upper()
            if lbank_coin == i:
                coins_prices[i]["LBank"] = float(lp["ticker"]["latest"])

        for mp in mexc_tickers:
            mexc_coin = mp["symbol"].replace("_", "").upper()
            if mexc_coin == i:
                coins_prices[i]["MEXC"] = float(mp["price"])

        for binp in binance_tickers:
            binance_coin = binp["symbol"].replace("_", "").upper()
            if binance_coin == i:
                coins_prices[i]["Binance"] = float(binp["price"])

        for kt in kucoin_tickers:
            kucoin_coin = kt["symbol"].replace("_", "").upper()
            if kucoin_coin == i:
                coins_prices[i]["MEXC"] = float(kt["price"])
    return coins_prices


def calc():
    all_spread = []
    # Выводим полученный словарь
    for keys, values in prices().items():
        min_b = ""
        max_b = ""
        price_list = list(values.values())
        min_price = min(price_list)
        max_price = max(price_list)
        for key, value in values.items():
            if value == min_price:
                min_b = key
            elif value == max_price:
                max_b = key
        all_spread.append([keys, min_b, min_price, max_b, max_price])
    return all_spread


print(time.time() - start_time)
