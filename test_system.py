import telebot
from telebot import types
import sqlalchemy
import random


class TestingSystem:
    def __init__(self, bot):
        self.bot = bot

    def choose_train(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("test1")
        btn2 = types.KeyboardButton("test2")
        help_btn = types.KeyboardButton("🧭 Помощь по режимам")
        menu_btn = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, help_btn, menu_btn)
        self.bot.send_message(message.chat.id,
                         text="Вы выбрали уровень {}\n\nВыберите режим".format(
                             message.text), reply_markup=markup)

    def get_info(self):
        pass

    def study_loop(self, message):
        test_count = 0
        while message.text != 'Выйти' or test_count != 10:
            pass
