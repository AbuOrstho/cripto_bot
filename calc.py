import spread
import json
import all_fees.fee as fee


coin_list = spread.calc()

bitmart_commission = json.load(open(r'BitMart\response_1.json', 'r', encoding="UTF-8"))
coinex_commission = json.load(open(r'Coinex\response_2.json', 'r', encoding="UTF-8"))
huobi_commission = json.load(open(r'Huobi\response_1.json', 'r', encoding="UTF-8"))
lbank_commission = json.load(open(r'LBank\response_1.json', 'r', encoding="UTF-8"))
mexc_commission = json.load(open(r'MEXC\response_1.json', 'r', encoding="UTF-8"))


def final_result():
    for i in coin_list:
        if i[1] == "Coinex" or i[3] == "Coinex":
            fees = coinex_commission["data"][i[0]]
            print(i)
            print(fees["maker_fee_rate"], fees["taker_fee_rate"])

        spread = ((i[4] - i[2]) / i[2]) * 100
        if spread > 5:
            continue
        else:
            p = 10000
            print(f"Пара {i[0]}\n"
                  f"Минимальная цена: {i[2]} на бирже: {i[1]}\n"
                  f"Максимальная цена: {i[4]} на бирже: {i[3]}\n"
                  f"Спред: {spread - 0.001 - 0.001}%\n"
                  f"Комиссия тейкера: {0.001}%\n"
                  f"Комиссия мейкера: {0.001}%\n"
                  f"Комиссия за сеть: {fee.fee()} USDT\n"
                  f"При начальной сумме в {p} итог: {(p / 100 * (spread - 0.001 - 0.001) - 1)}")
            print()
            print()
            print()


final_result()
