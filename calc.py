import spread

coin_list = spread.calc()

for i in coin_list:
    spread = ((i[4] - i[2]) / i[2]) * 100
    if spread > 5:
        continue
    else:
        print(f"Пара {i[0]}\n"
              f"Минимальная цена: {i[2]} на бирже: {i[1]}\n"
              f"Максимальная цена: {i[4]} на бирже: {i[3]}\n"
              f"Спред: {spread}%")
        print()
        print()
        print()