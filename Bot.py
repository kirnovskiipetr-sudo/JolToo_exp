import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUQz5CXGpN6v1p80'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
def get_main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn_wallet = KeyboardButton("💰 Кошелек JolToo.exp")
    btn_deposit = KeyboardButton("📥 Пополнить")
    btn_withdraw = KeyboardButton("📤 Вывести")
    keyboard.add(btn_wallet)
    keyboard.add(btn_deposit, btn_withdraw)
    return keyboard
    @dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"Добро пожаловать в {message.bot.id}! \nЭто твой крипто-кошелек JolToo.exp.",
        reply_markup=get_main_menu()
        dp.message_handler(lambda message: message.text == "💰 Кошелек JolToo.exp")
async def show_balance(message: types.Message):
    # Здесь позже мы подключим API для реального баланса
    await message.answer("Твой баланс: 0.00 USDT \n(Демо-режим)")

@dp.message_handler(lambda message: message.text == "📥 Пополнить")
async def deposit_crypto(message: types.Message):
    await message.answer("Выберите валюту для пополнения: \n1. BTC \n2. TON \n3. USDT")

@dp.message_handler(lambda message: message.text == "📤 Вывести")
async def withdraw_crypto(message: types.Message):
    await message.answer("Введите адрес кошелька и сумму для вывода:")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
