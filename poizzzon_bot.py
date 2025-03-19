import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot('8199250140:AAGYfBxICy0auIuoNiUbvIlNwI5x9-RN7Vo')

# Создаём клавиатуру
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Сделать заказ"), KeyboardButton("Отследить заказ"), KeyboardButton("Актуальный курс"), KeyboardButton("Рассчитать стоимость заказа"))

@bot.message_handler(func=lambda message: message.text == "/start")
def help_message(message):
    bot.send_message(message.chat.id, "Привет! 👋 Я бот для заказа товаров с Poizon.\n✅ Помогу оформить заказ, рассчитать стоимость и узнать актуальный курс.\nСледи за своим заказом в пару кликов!", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Сделать заказ")
def zakaz(message):
    bot.send_message(message.chat.id, "Готов оформить заказ или остались вопросы?\nПиши сюда @GlRu_71\nДля оформления заказа тебе нужно отправить ссылку на товар + указать свой размер", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Отследить заказ")
def track(message):
    bot.send_message(message.chat.id, "Отследить заказ можно, воспользовавшись этим сервисом: \nhttps://www.1track.ru/", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Актуальный курс")
def kurs(message):
    bot.send_message(message.chat.id, "1¥ = 13,75₽", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Рассчитать стоимость заказа")
def request_price(message):
    exit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    exit_keyboard.add(KeyboardButton("Отмена"))
    bot.send_message(message.chat.id, "Введите стоимость товара в Юанях:", reply_markup=exit_keyboard)
    bot.register_next_step_handler(message, calculate_price)

def calculate_price(message):
    if message.text == "Отмена":
        bot.send_message(message.chat.id, "Расчёт стоимости отменён.", reply_markup=keyboard)
        return
    try:
        price_yuan = float(message.text)
        price_rub = price_yuan * 13.75 + 3850
        bot.send_message(message.chat.id, f"Cтоимость заказа: {price_rub}₽ + 1000 ₽/кг\nНекоторые пары под заказ, может быть скидка, поэтому за уточнением 100% цены в ЛС @GlRu_71", reply_markup=keyboard)
    except ValueError:
        exit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        exit_keyboard.add(KeyboardButton("Отмена"))
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение стоимости товара в Юанях:", reply_markup=exit_keyboard)
        bot.register_next_step_handler(message, calculate_price)

@bot.message_handler(func=lambda message: message.text == "гойда")
def goida(message):
    bot.send_message(message.chat.id, "гойда", reply_markup=keyboard)

bot.infinity_polling()
