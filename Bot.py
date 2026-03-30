import asyncio, logging, aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUqz5CXGpN6v1p80'
CRYPTO_TOKEN = '559608:AAVdPFhXVM2jPuYQSUcnwY90RzxIzldnkLh'

logging.basicConfig(level=logging.INFO)
bot, dp = Bot(token=API_TOKEN), Dispatcher()

def get_menu():
    kb =,]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

@dp.message(Command("start"))
async def start(m: types.Message):
    await m.answer("JolToo.exp запущен!", reply_markup=get_menu())

@dp.message(F.text == "💰 Кошелек")
async def bal(m: types.Message):
    await m.answer("Баланс: 0.00 USDT")

@dp.message(F.text == "📥 Пополнить")
async def pay(m: types.Message):
    h = {'Crypto-Pay-API-Token': CRYPTO_TOKEN}
    async with aiohttp.ClientSession() as s:
        async with s.post('https://pay.crypt.bot', headers=h, json={'asset':'USDT','amount':'1'}) as r:
            res = await r.json()
            url = res['result']['pay_url'] if res.get('ok') else "Ошибка API"
            await m.answer(f"Оплата: {url}")

async def main(): await dp.start_polling(bot)
if __name__ == '__main__':... asyncio.run(main())
