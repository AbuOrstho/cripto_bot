import spread
import json
import all_fees.fee as fee

coin_list = spread.calc()

binance_tickers = json.load(open(r'Binance\response_all_tickers.json', 'r', encoding="UTF-8"))  # 1
bitfinex_tickers = json.load(open(r'Bitfinex\response_all_tickers.json', 'r', encoding="UTF-8"))  # 2
bitmart_tickers = json.load(open(r'BitMart\response_all_tickers.json', 'r', encoding="UTF-8"))  # 3
coinex_tickers = json.load(open(r'Coinex\response_all_tickers.json', 'r', encoding="UTF-8"))  # 4
huobi_tickers = json.load(open(r'Huobi\response_all_tickers.json', 'r', encoding="UTF-8"))  # 5
kraken_tickers = json.load(open(r'Kraken\response_all_tickers.json', 'r', encoding="UTF-8"))  # 6
kucoin_tickers = json.load(open(r'KuCoin\response_all_tickers.json', 'r', encoding="UTF-8"))  # 7
lbank_tickers = json.load(open(r'LBank\response_all_tickers.json', 'r', encoding="UTF-8"))  # 8
mexc_tickers = json.load(open(r'MEXC\response_all_tickers.json', 'r', encoding="UTF-8"))  # 9


def final_result():
    max_spread = ""
    max_number_spread = 0
    for i in coin_list:
        current_spread = ((i[4] - i[2]) / i[2]) * 100
        if current_spread > max_number_spread and current_spread <= 5:
            max_number_spread = current_spread
            p = 10000
            max_spread += f"""Пара {i[0]}
Минимальная цена: {i[2]} на бирже: {i[1]}
Максимальная цена: {i[4]} на бирже: {i[3]}
Спред: {current_spread - 0.001 - 0.001}%
Комиссия тейкера: {0.001}%
Комиссия мейкера: {0.001}%
Комиссия за сеть: {fee.fee()} USDT
При начальной сумме в {p} итог: {(p / 100 * (current_spread - 0.001 - 0.001) - 1)}


"""

    return max_spread
