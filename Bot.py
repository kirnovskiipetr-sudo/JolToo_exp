import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUqz5CXGpN6v1p80'
CRYPTO_TOKEN = '559608:AAVdPFhXVM2jPuYQSUcnwY9ORzxIzldnkLh'
'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("💰 Кошелек JolToo.exp"))
    keyboard.add(KeyboardButton("📥 Пополнить (1 USDT)"), KeyboardButton("📤 Вывести"))
    return keyboard
    @dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Добро пожаловать в JolToo.exp!", reply_markup=get_main_menu())

@dp.message_handler(lambda message: message.text == "💰 Кошелек JolToo.exp")
async def show_balance(message: types.Message):
    await message.answer("Ваш баланс: 0.00 USDT")

@dp.message_handler(lambda message: message.text == "📥 Пополнить (1 USDT)")
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
                await message.answer("Ошибка! Проверь CRYPTO_TOKEN в коде.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
