from exam import Exam
import telebot

# Exam Block
quiz = { 
    "Сколько океанов на нашей планете?": ["5", "4", "6"],
    "Единица измерения силы тока - это:": ["Ампер", "Вольт", "Ватт"],
    "Сатурн - это какая по счету планета от Солнца?": ["6", "7", "8"],
    "Какой элемент периодической системы химических элементов обозначается как Ag?": ["Серебро", "Золото", "Аргон"],
    "Сколько будет 0,2 км в дециметрах?": ["2 000 дм", "20 000 дм", "200 дм"],
    "Самая длинная в мире река - это:": ["Амазонка", "Нил", "Янцзы"],
    "В каком предложении допущена ошибка?": ["На полке лежала пачка макаронов", "Эти кремы просрочены", "На ней не было чулок"],
    "Зеленый пигмент, окрашивающий листья растений, называется:": ["Хлорофилл", "Хлоропласт", "Хлорофиллипт"],
    "Желчь образуется в:": ["Печени", "Желчном пузыре", "Поджелудочной железе"],
    "Сколько хромосом в геноме человека?": ["46", "42", "44"]
}

user = {
    "id": 54353,
    "nick": "Lik Eduard"
}

options = {
    "time": 30,
    "point": 1
}

# Initialization Exam
exam = Exam("exam.db")
loader = exam.loader(324325)

exam.export(name="Test1", exam=quiz, minutes=30, points=1)


exam.register(user)
















'''
# Telegram Block
token = open("token.txt", "r").read()
bot = telebot.TeleBot(token)
me = bot.get_me()

#--- Functions ---#
def setKeyBoard(*args):
    if args is None:
        return telebot.types.ReplyKeyboardRemove()
    kb = telebot.types.ReplyKeyboardMarkup()
    kb.row(*args)
    return kb

def sendQuestion(user):
    point = exam.getQuestion(user)
    info = exam.getUserInfo(user)
    bot.send_message(user, point.question(), reply_markup=setKeyBoard(*point.answers()))
#-----------------#

@bot.message_handler(commands=['start'])
def start_handler(message):
    user = message.chat.id
    bot.send_message(user, 'День добрый, друг! {} сегодня проводит небольшое тестирование, в котором ты можешь кое-что получить. Тебе нужно правильно ответить на все вопросы. Если ты готов, то нажми "Начать тестирование!".'.format(me.first_name), reply_markup=setKeyBoard("Начать тестирование!"))

@bot.message_handler(content_types=['text'])
def testing_handler(message):
    user = message.chat.id
    if message.text == "Начать тестирование!":
        sendQuestion(user)
    else:
        answers = exam.getQuestion(user).answers()
        if message.text in answers:
            exam.sendAnswer(user, message.text)
        sendQuestion(user)

@bot.message_handler(commands=['finish'])
def finish_handler(message):
    bot.send_message(message.chat.id, "Тестирование закончено!", reply_markup=setKeyBoard())


bot.polling(none_stop=True)
'''