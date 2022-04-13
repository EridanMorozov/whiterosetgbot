# Импортируем необходимые классы.
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(update.message.text)

    # Мужик спрашивает у мусульманина: — Слушай, вот никак не могу понять, зачем вашим женщинам эта тряпка на голове
    # - паранджа или как её?... Лица не видно, дышать невозможно, есть сложно... Ну нафига? Мусульманин молча достаёт
    # из кармана две шоколадные конфеты и протягивает на ладони. Одна в обёртке, другая без. Та, что без фантика,
    # уже слегка облупившаяся, к ней какой-то мусор из кармана прилип, крошки... — Вот ты бы какую выбрал? Мужик
    # задумывается, чешет в голове, и отвечает: — Ну, я бы эту. Берёт конфету в обёртке, разворачивает и взрывается.

def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater('5264916178:AAFVw-7R1T_H7b-_tgfwoGby3p6YLahvgoY', use_context=True)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher
    # Зарегистрируем их в диспетчере рядом
    # с регистрацией обработчиков текстовых сообщений.
    # Первым параметром конструктора CommandHandler я
    # вляется название команды.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("Translate", translate))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("select_lvl", lvl))
    dp.add_handler(CommandHandler("site", site))
    dp.add_handler(CommandHandler("work_time", work_time))
    dp.add_handler(CommandHandler("close", close_keyboard))  # закрытие клавиатуры
    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)
    # Регистрируем обработчик в диспетчере.
    dp.add_handler(text_handler)
    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.
def start(update, context):
    update.message.reply_text(
        "Я - бот переводчик! Я помогу тебе в изучении английского языка!"
        " Напиши /help для получения справки о работе с ботом.",
        reply_markup=markup
    )


def translate(update, context):
    update.message.reply_text(
        "Я пока не умею переводить... Я только ваше эхо.")


def help(update, context):
    update.message.reply_text(
        "Справка по кнопкам:"
        " /translate - позволяет перевести предложение"
        " /selectlvl - дает вам выбрать уровень знания английского (А2, В1)"
        " /phrasal_verbs | /prepositional_phrases - вывод списка устойчивых выражений.")


def lvl(update, context):
    update.message.reply_text("Выберите ваш уровень в кнопках снизу:")


def site(update, context):
    update.message.reply_text(
        "Сайт: http://www.yandex.ru/company")


def work_time(update, context):
    update.message.reply_text(
        "График работы: 4:20 - 16:20")


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


reply_keyboard = [['/translate', '/help'],
                  ['/select_lvl']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
