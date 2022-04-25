# Импортируем необходимые классы.
import telebot
from telebot import types  # для указание типов
import config
import translator as tr
import database as db
import logging

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s")
bot = telebot.TeleBot(config.telegram_token)
print('start')


@bot.message_handler(commands=['start'])
def start_bot(message):
    if db.user_exist(message.chat.id):
        bot.send_message(message.chat.id, 'Ви вже розпочинали бесіду з цим ботом.\n'
                                          'Для перегляду списку усіх команд скористайтеся '
                                          'командою - /help.')
    else:
        user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                one_time_keyboard=True)
        sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
        for lang in sorted_langs:
            user_markup.row(lang[1])
        msg = bot.send_message(message.chat.id,
                               'Здравствуй! \nЭто бот-переводчик и помощник, который '
                               'построен на Yandex-переводчике и поддерживает более '
                               '90 языков мира. \nПомимо переводчика вы можете еще и узнать множество фраз, которые '
                               'украсят вашу речь на английском языке, используя команду select_lvl! '
                               ' \nТеперь вам необходимо указать язык, на который переводится текст. '
                               '\nИзменить язык перевода можно с помощью команды '
                               '/langs (все языки) и /top_langs (популярные языки). '
                               '\nЯзык входного текста определяется автоматически. '
                               '\nСписок всех команд Вы можете просмотреть в меню команд, '
                               'находящийся возле клавиши отправки сообщения.', reply_markup=user_markup)

        def add_user(msg):
            usr_lang = msg.text
            db.add_user(msg.chat.id, usr_lang)
            hide_markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Чудово!', reply_markup=hide_markup)

        bot.register_next_step_handler(msg, add_user)


@bot.message_handler(commands=['langs'])
def change_langs(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Выберите язык:',
                           reply_markup=user_markup)

    def change(msg):
        usr_lang = msg.text
        db.change_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Язык успешно заменён!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)


@bot.message_handler(commands=['top_langs'])
def change_langs(message):
    user_markup = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    sorted_langs = sorted(db.top_langs.items(), key=lambda kv: kv[1])
    for lang in sorted_langs:
        user_markup.row(lang[1])
    msg = bot.send_message(message.chat.id,
                           'Выберите язык:',
                           reply_markup=user_markup)

    def change(msg):
        usr_lang = msg.text
        db.change_top_langs(msg.chat.id, usr_lang)
        hide_markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Язык успешно заменён!',
                         reply_markup=hide_markup)

    bot.register_next_step_handler(msg, change)


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Поздороваться":
        bot.send_message(message.chat.id,
                         text="Я - бот переводчик! Я помогу тебе в изучении английского языка!")
    elif message.text == "🧭 Помощь":
        bot.send_message(message.chat.id, text="Выберите уровень знаний английского, используя кнопки внизу!")
    elif message.text == "❓ Выбор уровня":
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
        button2 = types.KeyboardButton("❓ Выбор уровня")
        button3 = types.KeyboardButton("🧭 Помощь")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         text="На такую команду я не запрограммировал.. Если не знаешь что спросить, то напиши "
                              "кнопку 'Помощь'.")




bot.polling(none_stop=True)
