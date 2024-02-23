import time
import asyncio
import sys

start_time = time.time()

# Предполагаем, что эти импорты относятся к вашим модулям и они уже адаптированы под асинхронный запуск
from Binance.Binance import binance
from Bitfinex.Bitfinex import bitfinex
from BitMart.BitMart import bitmart
from Coinex.Coinex import coinex
from Huobi.Huobi import huobi
from Kraken.Kraken import kraken
from KuCoin.KuCoin import kucoin
from LBank.LBank import lbank
from MEXC.MEXC import mexc

from calc import final_result

async def main():
    start_time = time.time()

    # Предполагаем, что run методы асинхронные и можно вызвать await на них
    await asyncio.gather(
        binance.run(),
        bitfinex.run(),
        bitmart.run(),
        coinex.run(),
        huobi.run(),
        kraken.run(),
        kucoin.run(),
        lbank.run(),
        mexc.run()
    )

    print(f"Время выполнения: {time.time() - start_time} секунд.")


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
print(final_result())
print(time.time() - start_time)