import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUqz5CXGpN6v1p80'
CRYPTO_TOKEN = '559608:AAVdPFhXVM2jPuYQSUcnwY90RzxIzldnkLh'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: types.Message):
    b1 = types.KeyboardButton(text="💰 Кошелек")
    b2 = types.KeyboardButton(text="📥 Пополнить")
    nav = types.ReplyKeyboardMarkup(
        keyboard=[[b1, b2]], 
        resize_keyboard=True
    )
    await m.answer("Бот JolToo.exp запущен!", reply_markup=nav)

@dp.message(F.text == "💰 Кошелек")
async def bal(m: types.Message):
    await m.answer("Ваш баланс: 0.00 USDT")

@dp.message(F.text == "📥 Пополнить")
async def pay(m: types.Message):
    h = {'Crypto-Pay-API-Token': CRYPTO_TOKEN}
    async with aiohttp.ClientSession() as s:
        async with s.post('https://pay.crypt.bot/api/createInvoice', headers=h, json={'asset':'USDT','amount':'1'}) as r:
            res = await r.json()
            if res.get('ok'):
                url = res['result']['pay_url']
                await m.answer(f"Ссылка на оплату 1 USDT: {url}")
            else:
                await m.answer("Ошибка API.")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
