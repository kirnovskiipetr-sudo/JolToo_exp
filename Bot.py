import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
import aiohttp
API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUqz5CXGpN6v1p80'
CRYPTO_TOKEN = '559608:AAVdPFhXVM2jPuYQSUcnwY90RzxIzldnkLh'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
def get_main_menu():
    buttons =,
    return types.ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать в JolToo.exp!", reply_markup=get_main_menu())
@dp.message(F.text == "💰 Кошелек JolToo.exp")
async def show_balance(message: types.Message):
    await message.answer("Ваш баланс: 0.00 USDT")
@dp.message(F.text == "📥 Пополнить (1 USDT)")
async def deposit_crypto(message: types.Message):
    headers = {'Crypto-Pay-API-Token': CRYPTO_TOKEN}
    data = {'asset': 'USDT', 'amount': '1'}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://pay.crypt.bot', headers=headers, json=data) as resp:
            res = await resp.json()
            if res.get('ok'):
                url = res['result']['pay_url']
                await message.answer(f"Оплати 1 USDT здесь: {url}")
            else:
                await message.answer("Ошибка в CryptoPay API!")
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())
