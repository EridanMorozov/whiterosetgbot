langs = {'cy': 'Валлийский', 'tl': 'Тагальский', 'sk': 'Словацкий',
         'bg': 'Болгарский', 'ml': 'Малаялам', 'sr': 'Сербский', 'jv': 'Яванский',
         'ar': 'Арабский', 'mt': 'Мальтийский', 'tr': 'Турецкий', 'tg': 'Таджицкий',
         'lo': 'Лаоский', 'id': 'индонезийский', 'pl': 'Польский',
         'az': 'Азербайджанский', 'el': 'Грецкий', 'ca': 'Каталанский',
         'fa': 'Перский', 'cs': 'Ческий', 'kn': 'Каннада', 'en': 'Английский',
         'mg': 'Малагасийский', 'gl': 'Галисийский', 'my': 'Бирманский',
         'la': 'Латина', 'uk': 'Украинский', 'ka': 'Грузинский', 'ru': 'Русский',
         'no': 'Норвезкий', 'si': 'Сингальский', 'pap': "Пап'яменто",
         'lv': 'Латиский', 'gu': 'Гуджарати', 'bs': 'Боснийский',
         'mrj': 'Гирськомарийский', 'ta': 'Тамильский', 'ur': 'Урду',
         'su': 'Сунданский', 'mk': 'Македонский', 'ky': 'Киргизкий',
         'pa': 'Пенджабский', 'sv': 'Шведский', 'hu': 'Угорский', 'ko': 'Корейский',
         'zh': 'Китайский', 'sw': 'Суахили', 'eu': 'Баскский',
         'nl': 'Нидерландский', 'he': 'Иврит', 'udm': 'Удмуртский',
         'ga': 'Ирландский', 'hy': 'Вирменский', 'th': 'Тайский', 'xh': 'Коса',
         'kk': 'Казахский', 'lt': 'Литовский', 'af': 'Африкаанс',
         'tt': 'Татарский', 'ja': 'Японский', 'ro': 'Румынский', 'de': 'Немецкий',
         'uz': 'Узбекский', 'sq': 'Албанский', 'it': 'италийский', 'fi': 'Финский',
         'bn': 'Бенгальский', 'hr': 'Хорватский', 'is': 'исландский',
         'mn': 'Монгольский', 'te': 'Телугу', 'mr': 'Маратхи', 'ht': 'Гаитянский',
         'fr': 'Французкий', 'eo': 'Есперанто', 'be': 'Белорусский', 'et': 'Эстонский',
         'pt': 'Португальский', 'mi': 'Маори', 'es': 'испанский', 'da': 'Данский',
         'ceb': 'Себуанский', 'am': 'Амхарский', 'ne': 'Непальский', 'ms': 'Малайский',
         'ba': 'Башкирский', 'sl': 'Словенский', 'km': 'Кхмерский', 'mhr': 'Марийский',
         'hi': 'Хинди', 'yi': 'идиш', 'lb': 'Люксембурзкий', 'vi': "Вьєтнамский",
         'gd': 'Шотландский (гельский)'}


top_langs = {'en': 'Английский', 'it': 'италийский', 'de': 'Нимецкий',
             'fr': 'Французкий', 'pl': 'Польский', 'es': 'испанский',
             'uk': 'Украинский', 'ru': 'Русский'}

users_data = {}

def user_exist(chat_id):
    if str(chat_id) in users_data:
        return True
    else:
        return False

def add_user(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(langs.keys())[list(langs.values()).index(str(usr_lang))])

def change_top_langs(chat_id, usr_lang):
    users_data[str(chat_id)] = \
        str(list(top_langs.keys())[list(top_langs.values()).index(str(usr_lang))])