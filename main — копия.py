# Импортируем необходимые классы.
import telebot
from telebot import types  # для указание типов
import config
import logging
from data import db_session
from test_system import TestingSystem

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
logging.info('start')
bot = telebot.TeleBot(config.token)
levels = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
testSystem = TestingSystem(bot)
db_session.global_init("db/bot.db")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("❓ Выбор уровня английского")
    help_btn = types.KeyboardButton("🧭 Помощь")
    markup.add(btn2, help_btn)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я - бот переводчик! Я помогу тебе в изучении английского языка!".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main_loop(message):

    if message.text == "🧭 Помощь" or message.text == 'Помощь':
        bot.send_message(message.chat.id, text="Выберите необходимую вам команду в выпадающем списке <text>.\n\n"
                                               "Команда 'Выбор уровня английского' - вам предлагается выбрать "
                                               "ваш уровень знания английского языка. Всего существует 6 уровней языка,"
                                               "начиная от А1 (начальный), заканчивая С2 (профессиональный) \n\n"
                                               "Команда <translate mb, esli makar sdelaet> - <text>")

    elif message.text == "🧭 Помощь по режимам":
        bot.send_message(message.chat.id, text=" Режим 'Изучение слов' направлен на то, чтобы помочь вам"
                                               "выучить новые слова из самых разных сфер жизни в форме теста."
                                               " \n\n"
                                               "Режим '' помогает вам <do2>")
    elif message.text in levels:
        lvl = message.text
        testSystem.choose_train(message)
        testSystem.study_loop(message)

    elif message.text == "❓ Выбор уровня английского":
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
                              "'Помощь' или нажмите на соответствующую кнопку.")


bot.polling(none_stop=True)
