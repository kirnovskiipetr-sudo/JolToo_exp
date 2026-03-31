import telebot
from telebot import types
import os

TOKEN = os.getenv ("8308105524:AAF4jlu0PGjpFQlylmiillnZSBNCmkUyWfI")

bot = telebot.TeleBot(TOKEN)

# --- ГЛАВНОЕ МЕНЮ ---
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎨 Наши работы", "🏠 О нас")
    markup.add("💰 Цены", "🎁 Розыгрыш")
    markup.add("📞 Связаться с дизайнером")
    markup.add("📝 Оставить заявку")
    return markup
    
    # --- СТАРТ ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в JolToo.exp!\n"
        "Мы создаем интерьеры, которые вдохновляют.\n\n"
        "Чем я могу вам помочь? 👇",
        reply_markup=main_menu()
    )

# --- НАШИ РАБОТЫ ---
@bot.message_handler(func=lambda m: m.text == "🎨 Наши работы")
def portfolio(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛋 Квартиры и дома", "☕️ Кафе и офисы")
    markup.add("✨ Реализованные объекты")
    markup.add("⬅️ Назад в меню")

    bot.send_photo(
    message.chat.id,
    "ССЫЛКА_НА_ФОТО", "https://t.me/c/3865067942/6"

    caption="Пример проекта JolToo.exp"
)
     bot.send_message(  
     message.chat.id,
        "📂 Портфолио JolToo.exp\n"
        "Выберите категорию:",
        reply_markup=markup
    )
    
    # --- О НАС ---
@bot.message_handler(func=lambda m: m.text == "🏠 О нас")
def about(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("👨‍🎨 Наша команда", "📝 Этапы работы")
    markup.add("⬅️ Назад в меню")

    bot.send_message(
        message.chat.id,
        "✨ Коротко о нашей студии\n"
        "Мы создаем стильные и функциональные интерьеры.\n"
        "Работаем по договору и соблюдаем сроки.",
        reply_markup=markup
    )


# --- ЦЕНЫ ---
@bot.message_handler(func=lambda m: m.text == "💰 Цены")
def prices(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🧮 Рассчитать проект", "📥 Скачать прайс-лист")
    markup.add("⬅️ Назад в меню")

    bot.send_message(
        message.chat.id,
        "📊 Стоимость услуг:\n\n"
        "1️⃣ Планировка — от 10$/м²\n"
        "2️⃣ Эскиз — от 20$/м²\n"
        "3️⃣ Полный дизайн — от 40$/м²\n\n"
        "Нажмите ниже для расчета 👇",
        reply_markup=markup
    )


# --- РОЗЫГРЫШ ---
@bot.message_handler(func=lambda m: m.text == "🎁 Розыгрыш")
def giveaway(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("✅ Участвовать", "📜 Полные правила")
    markup.add("⬅️ Назад в меню")

    bot.send_message(
        message.chat.id,
        "🎉 Розыгрыш!\n\n"
        "Выиграй бесплатную консультацию.\n\n"
        "Условия:\n"
        "1. Подписка на канал\n"
        "2. Нажать участвовать\n\n"
        "Итоги скоро!",
        reply_markup=markup
    )


# --- КНОПКА НАЗАД ---
@bot.message_handler(func=lambda m: m.text == "⬅️ Назад в меню")
def back(message):
    bot.send_message(
        message.chat.id,
        "Главное меню 👇",
        reply_markup=main_menu()
    )


# --- ПОЛУЧЕНИЕ НОМЕРА ---
@bot.message_handler(content_types=['contact'])
def get_contact(message):
    phone = message.contact.phone_number
    user_name = message.from_user.first_name

    ADMIN_ID = 123456789  # ← ВСТАВЬ СВОЙ ID

    # отправка тебе
    bot.send_message(
        ADMIN_ID,8668859962
        f"🔥 Новый клиент!\n\nИмя: {user_name}\nТелефон: {phone}"
    )

    # ответ пользователю
    bot.send_message(
        message.chat.id,
        "✅ Спасибо! Мы скоро с вами свяжемся."
    )


# --- ЗАПУСК ---
print("Бот запущен...")
bot.polling(none_stop=True)
