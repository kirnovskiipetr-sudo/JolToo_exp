import telebot
from telebot import types
import os
import threading
from flask import Flask

# --- МИНИ-СЕРВЕР ДЛЯ RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Bot is Live!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- КОД БОТА JolToo.exp ---
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
    bot.send_message(message.chat.id, "👋 Привет! Это JolToo.exp.\nИзучите наше портфолио или закажите проект прямо здесь 👇", reply_markup=main_menu())

# --- РАЗДЕЛ НАШИ РАБОТЫ (КАТЕГОРИИ) ---
@bot.message_handler(func=lambda m: m.text == "🎨 Наши работы")
def portfolio_categories(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("🌐 Сайты", "🤖 Боты")
    markup.add("🖼 Баннеры", "💎 Под ключ")
    markup.add("⬅️ Назад в меню")
    bot.send_message(message.chat.id, "Выберите категорию проектов:", reply_markup=markup)

# --- ЛОГИКА ДЛЯ КАТЕГОРИЙ ---

@bot.message_handler(func=lambda m: m.text == "🌐 Сайты")
def category_sites(message):
    # Замени "ССЫЛКА" на реальную ссылку на фото работы
    photo_url = "https://i.ibb.co/vz6007L/joltoo-exp.jpg" 
    caption = "🌐 **Наши сайты**\n\nРазработка современных лендингов и многостраничников.\n\n✅ Адаптивный дизайн\n✅ Высокая скорость загрузки"
    bot.send_photo(message.chat.id, photo_url, caption=caption, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🤖 Боты")
def category_bots(message):
    photo_url = "https://i.ibb.co/vz6007L/joltoo-exp.jpg"
    caption = "🤖 **Telegram боты**\n\nСоздаем ботов-визиток, магазинов и систем автоматизации.\n\n✅ Интеграция с платежами\n✅ Удобное меню"
    bot.send_photo(message.chat.id, photo_url, caption=caption, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "🖼 Баннеры")
def category_banners(message):
    photo_url = "https://i.ibb.co/vz6007L/joltoo-exp.jpg"
    caption = "🖼 **Дизайн баннеров**\n\nКреативы для соцсетей и рекламы, которые привлекают внимание.\n\n✅ Уникальный стиль\n✅ Продающие смыслы"
    bot.send_photo(message.chat.id, photo_url, caption=caption, parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "💎 Под ключ")
def category_full(message):
    photo_url = "https://i.ibb.co/vz6007L/joltoo-exp.jpg"
    caption = "💎 **Проекты под ключ**\n\nПолная упаковка вашего бренда: от логотипа до сайта и бота.\n\n✅ Единый стиль\n✅ Максимальная выгода"
    bot.send_photo(message.chat.id, photo_url, caption=caption, parse_mode="Markdown")

# --- ОСТАЛЬНЫЕ ФУНКЦИИ ---
@bot.message_handler(func=lambda m: m.text == "⬅️ Назад в меню")
def back_home(message):
    bot.send_message(message.chat.id, "Главное меню 👇", reply_markup=main_menu())

@bot.message_handler(func=lambda m: m.text == "💰 Цены")
def prices(message):
    bot.send_message(message.chat.id, "🔹 CORE — $100\n🔹 FLOW — $250\n🔹 GOD MODE — от $400", parse_mode="Markdown")

@bot.message_handler(func=lambda m: m.text == "📞 Связаться с дизайнером")
def designer_contacts(message):
    bot.send_message(message.chat.id, "✈️ Telegram: @joltooexp\n💬 WhatsApp: https://wa.me/996502882882")

@bot.message_handler(func=lambda m: m.text == "📝 Оставить заявку")
def application(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton("📱 Отправить контакт", request_contact=True), "⬅️ Назад в меню")
    bot.send_message(message.chat.id, "Нажмите кнопку, чтобы мы связались с вами!", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    bot.send_message(8668859962, f"🔥 ЗАЯВКА!\nИмя: {message.contact.first_name}\nТел: {message.contact.phone_number}")
    bot.send_message(message.chat.id, "✅ Получили! Скоро свяжемся.", reply_markup=main_menu())

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
