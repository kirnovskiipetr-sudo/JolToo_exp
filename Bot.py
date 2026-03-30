import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

# Токены (лучше хранить в .env, но оставляем как в примере)
API_TOKEN = '8308105524:AAF8BG64FyxOiHFxcxjSUqz5CXGpN6v1p80'
CRYPTO_TOKEN = '559608:AAVdPFhXVM2jPuYQSUcnwY90RzxIzldnkLh'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(m: types.Message):
    # Создаем кнопки 🔘
    b1 = types.KeyboardButton(text="💰 Кошелек")
    b2 = types.KeyboardButton(text="📥 Пополнить")
    
    # Собираем меню (список списков для рядов)
    nav = types.ReplyKeyboardMarkup(
        keyboard=[
            [b1, b2]  # Оба в одном ряду
        ], 
        resize_keyboard=True
    )
    
    await m.answer("Бот JolToo.exp запущен!", reply_markup=nav)

@dp.message(F.text == "💰 Кошелек")
async def bal(m: types.Message):
    await m.answer("Ваш баланс: 0.00 USDT")

@dp.message(F.text == "📥 Пополнить")
async def pay(m: types.Message):
    # Заголовок для API Crypto Bot 💳
    h = {'Crypto-Pay-API-Token': CRYPTO_TOKEN}
    
    async with aiohttp.ClientSession() as s:
        # Исправленный URL для создания счета (createInvoice)
        async with s.post('https://pay.crypt.bot/api/createInvoice', headers=h, json={'asset':'USDT','amount':'1'}) as r:
            res = await r.json()
            if res.get('ok'):
                url = res['result']['pay_url']
                await m.answer(f"Ссылка на оплату 1 USDT: {url}")
            else:
                error_msg = res.get('error', {}).get('name', 'Неизвестная ошибка')
                await m.answer(f"Ошибка API: {error_msg}")

async def main():
    # Удаляем вебхуки перед запуском, чтобы не было конфликтов
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
