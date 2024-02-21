import time
import asyncio
import sys

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
from OKX.OKX import okx
from Poloniex.Poloniex import poloniex


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
        mexc.run(),
        okx.run(),
        poloniex.run()
    )

    print(f"Время выполнения: {time.time() - start_time} секунд.")


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
