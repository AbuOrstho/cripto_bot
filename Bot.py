from aiogram import Bot, Dispatcher, types, executor
import asyncio
import sys

# Здесь предполагается, что ваши модули адаптированы под асинхронный запуск
from Binance.Binance import binance
from Bitfinex.Bitfinex import bitfinex
from BitMart.BitMart import bitmart
from Coinex.Coinex import coinex
from Huobi.Huobi import huobi
from Kraken.Kraken import kraken
from KuCoin.KuCoin import kucoin
from LBank.LBank import lbank
from MEXC.MEXC import mexc

# Импорт вашего метода final_result
from calc import final_result

bot_token = ""
bot = Bot(bot_token)
dp = Dispatcher(bot)


async def find_best_trade():
    # Поместите сюда логику асинхронного сбора данных
    # Это пример, вам нужно будет адаптировать код под ваши модули
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
    # Предполагаем, что final_result() возвращает строку с результатами
    return final_result()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(
        f'Привет {message.from_user.first_name}! Используй команду /find_best_trade для поиска лучших торговых возможностей.')


@dp.message_handler(commands=['find_best_trade'])
async def handle_find_best_trade(message: types.Message):
    await message.reply("Ищем лучшие торговые возможности... Это может занять некоторое время.")
    result = await find_best_trade()
    await message.reply(result)


if __name__ == "__main__":
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    executor.start_polling(dp, skip_updates=True)
