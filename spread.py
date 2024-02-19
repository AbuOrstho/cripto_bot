import json
import time
from collections import Counter
import time

start_time = time.time()

bitmark_prices = json.load(open(r'BitMart\response_1.json', 'r', encoding="UTF-8"))["data"]["tickers"]
coinex_prices = json.load(open(r'Coinex\response_1.json', 'r', encoding="UTF-8"))["data"]["ticker"]
huobi_prices = json.load(open(r'Huobi\response_1.json', 'r', encoding="UTF-8"))["data"]
lbank_prices = json.load(open(r'LBank\response_1.json', 'r', encoding="UTF-8"))["data"]
mexc_prices = json.load(open(r'MEXC\response_1.json', 'r', encoding="UTF-8"))["symbols"]

all_token = json.load(open('url_lib.json', 'r', encoding='UTF-8'))  # Полный json файл

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []

for i in all_token["Coinex"]["coin"]:
    list1.append(i.upper().replace('_', ''))
for i in all_token["LBank"]["coin"]:
    list2.append(i.upper().replace('_', ''))
for i in all_token["MEXC"]["coin"]:
    list3.append(i.upper().replace('_', ''))
for i in all_token["BitMart"]["coin"]:
    list4.append(i.upper().replace('_', ''))
for i in all_token["Huobi"]["coin"]:
    list5.append(i.upper().replace('_', ''))

# Соберем все списки в один для анализа
all_lists = list1 + list2 + list3 + list4 + list5

# Подсчитаем, сколько раз каждый элемент встречается в объединенном списке
counter = Counter(all_lists)

# Найдем элементы, встречающиеся в 2, 3 и 4 списках
two_lists = [item for item, count in counter.items() if count == 2]
three_lists = [item for item, count in counter.items() if count == 3]
four_lists = [item for item, count in counter.items() if count == 4]
five_lists = [item for item, count in counter.items() if count == 5]

mexc_price = json.load(open(r'MEXC\response_2.json', 'r', encoding="UTF-8"))


def prices():
    # Инициализируем словарь для хранения результатов
    coins_prices = {}

    for i in five_lists:
        # Для каждой монеты создаем словарь с ценами на разных биржах
        coins_prices[i] = {}

        for bp in bitmark_prices:
            bitmark_coin = bp["symbol"].replace("_", "").upper()
            if bitmark_coin == i:
                coins_prices[i]["Bitmark"] = float(bp["last_price"])

        for cp in coinex_prices:
            coinex_coin = cp.replace("_", "").upper()
            if coinex_coin == i:
                coins_prices[i]["Coinex"] = float(coinex_prices[cp]['last'])

        for hp in huobi_prices:
            huobi_coin = hp["symbol"].replace("_", "").upper()
            if huobi_coin == i:
                coins_prices[i]["Huobi"] = float(hp["close"])

        for lp in lbank_prices:
            lbank_coin = lp['symbol'].replace("_", "").upper()
            if lbank_coin == i:
                coins_prices[i]["LBank"] = float(lp["ticker"]["latest"])

        for mp in mexc_price:
            mexc_coin = mp["symbol"].replace("_", "").upper()
            if mexc_coin == i:
                coins_prices[i]["MEXC"] = float(mp["price"])
    print(coins_prices)
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
