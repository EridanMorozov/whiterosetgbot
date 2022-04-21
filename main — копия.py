# Импортируем необходимые классы.
import telebot
from telebot import types  # для указание типов
import config
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
bot = telebot.TeleBot(config.token)
print('start')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Выбор уровня знания английского")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я - бот переводчик! Я помогу тебе в изучении английского языка!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id,
                         text="Я - бот переводчик! Я помогу тебе в изучении английского языка!")
    elif message.text == "❓ Выбор уровня знания английского":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("A1")
        btn2 = types.KeyboardButton("A2")
        btn3 = types.KeyboardButton("B1")
        btn4 = types.KeyboardButton("B2")
        btn5 = types.KeyboardButton("C1")
        btn6 = types.KeyboardButton("C2")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text="Выберите уровень знания английского", reply_markup=markup)

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Выбор уровня знания английского")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text="На такую команду я не запрограммировал.. Если не знаешь что спросить, то напиши "
                              "кнопку 'Помощь'.")


bot.polling(none_stop=True)
