import telebot
from telebot import types
import sqlalchemy
import random


class TestingSystem:
    def __init__(self, bot):
        self.bot = bot
        self.lvl = None

    def choose_train(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        self.lvl = message.text
        btn1 = types.KeyboardButton("test1")
        btn2 = types.KeyboardButton("test2")
        help_btn = types.KeyboardButton("🧭 Помощь по режимам")
        menu_btn = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, help_btn, menu_btn)
        self.bot.send_message(message.chat.id,
                         text="Вы выбрали уровень {}\n\nВыберите режим".format(
                             message.text), reply_markup=markup)

    def study(self):
        pass

    def test(self, message):
        self.bot.send_message(message.chat.id, text="Приветствуем в обучающем режиме <text>")
        answer = 1
        test_count = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(random.randint(1, 100))
        btn2 = types.KeyboardButton(random.randint(1, 100))
        btn3 = types.KeyboardButton(random.randint(1, 100))
        btn4 = types.KeyboardButton(random.randint(1, 100))
        back = types.KeyboardButton("Выйти")
        markup.add(btn1, btn2, btn3, btn4, back)
        self.bot.send_message(message.chat.id, text=f"function 'study'", reply_markup=markup)
        if message.text == answer:
            self.bot.send_message(message.chat.id, text=f"YES", reply_markup=markup)


