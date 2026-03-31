import telebot
from telebot import types
import os
import threading
from flask import Flask

# Настройка мини-сервера для Render (чтобы не было ошибки портов)
app = Flask('')
@app.route('/')
def home():
    return "Bot is Live!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- ОСНОВНОЙ КОД БОТА ---
TOKEN = "8308105524:AAF4jlu0PGjpFQlylmiillnZSBNCmkUyWfI"
bot = telebot.TeleBot(TOKEN)

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🎨 Наши работы", "🏠 О нас")
    markup.add("💰 Цены", "🎁 Розыгрыш")
    markup.add("📞 Связаться с дизайнером", "📝 Оставить заявку")
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Здравствуйте! Вас приветствует бот JolToo.exp!\n\n"
        "Выберите интересующий раздел в меню 👇",
        reply_markup=main_menu()
    )

@bot.message_handler(func=lambda m: m.text == "🎨 Наши работы")
def portfolio(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🖼 Дизайн и Лого", "📹 Видео и Reels")
        markup.add("✨ Реализованные объекты", "⬅️ Назад в меню")
    bot.send_message(message.chat.id, "📁 Выберите категорию проектов:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "✨ Реализованные объекты")
def real_objects(message):
    bot.send_message(
        message.chat.id, 
        "🏗 **Наши реализованные объекты**\n\n"
        "Раздел JolToo.exp находится в разработке. Скоро здесь появится галерея наших лучших проектов!\n\n"
        "Следите за обновлениями!",
        parse_mode="Markdown"
    )

        "Мы — студия креативного контента. Наша цель: делать ваш бренд узнаваемым.\n\n"
        "👩‍🎨 **О владелице:**\n"
        "Проект основан профессиональным дизайнером. Мы работаем на результат!",
        parse_mode="Markdown"
    )

@bot.message_handler(func=lambda m: m.text == "💰 Цены")
def prices(message):
    price_text = (
        "🚀 **Прайс JolToo.exp**\n\n"
        "🔹 **PACK: CORE — $100** (База)\n"
        "🔹 **PACK: FLOW — $250** (Актив)\n"
        "🔹 **PACK: GOD MODE — от $400** (Топ)\n\n"
        "⚡️ **Поштучно:**\n"
        "• Art — $20 | Video — $40 | Logo — $80"
    )
    bot.send_message(message.chat.id, price_text, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🎁 Розыгрыш")
def giveaway(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("📢 Наш Канал", url="https://t.me/+z18RcNUVOp9kNWQy"))
    bot.send_message(message.chat.id, "🎁 Подпишись на канал, чтобы участвовать!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "📞 Связаться с дизайнером")
def designer_contacts(message):
    contacts = (
        "👨‍🎨 **Контакты JolToo.exp:**\n\n"
        "✈️ Telegram: [Написать](https://t.me/joltooexp)\n"
        "💬 WhatsApp: [Написать](https://wa.me/996502882882)\n"
        "📸 Instagram: [Профиль](https://www.instagram.com/joltoo.exp?igsh=MWpkYWkycTJ4NDFsbw==)"
    )
    bot.send_message(message.chat.id, contacts, parse_mode="Markdown", disable_web_page_preview=True)

@bot.message_handler(func=lambda m: m.text == "📝 Оставить заявку")
def application(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("📱 Отправить свои данные", request_contact=True), "⬅️ Назад в меню")
    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы мы могли связаться с вами!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "⬅️ Назад в меню")
def back_home(message):
    bot.send_message(message.chat.id, "Главное меню 👇", reply_markup=main_menu())

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    bot.send_message(8668859962, f"🔥 **ЗАЯВКА!**\nИмя: {message.contact.first_name}\nТел: {message.contact.phone_number}")
    bot.send_message(message.chat.id, "✅ Мы получили данные и скоро свяжемся с вами!", reply_markup=main_menu())

# --- ЗАПУСК ---
if __name__ == "__main__":
    keep_alive() # Запуск фонового сервера для Render
    print("Бот JolToo запущен!")
    bot.polling(none_stop=True)
