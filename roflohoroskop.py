import telebot
from telebot import types
import random

bot = telebot.TeleBot('1435044477:AAGqMGbBf_1znBRl_6NHBjyYF9QtDEzc6JI')

first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того,"
         " чтобы решиться на смелый поступок!",
         "Будьте осторожны,"
         " сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того,"
         " чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того,"
         " чтобы разобраться с накопившимися делами."]

second = ["Но помните,"
          " что даже в этом случае нужно не забывать про",
          "Если поедете за город,"
          " заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел,"
          " должны помнить про",
          "Если у вас упадок сил,"
          " обратите внимание на",
          "Помните, что мысли материальны, а значит"
          " вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы,"
              " которые могут так некстати помешать планам.",
              "себя и своё здоровье, "
              "иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, "
              "которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя "
              "в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, "
         "но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, "
         "поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить"
         " влияние ретроградного Меркурия, "
         "то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то"
         " самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, "
         "и тогда эта встреча посулит вам приятные хлопоты."]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row('horoskope', 'auf')
    bot.send_message(message.chat.id, 'выберите кнопку', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_horoskope(message):
    if message.text.lower() == 'дева':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'рыбы':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'весы':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'телец':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'козерог':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'водолей':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'скорпион':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'овен':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'стрелец':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'лев':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'рак':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'близнецы':
        horoskope = random.choice(first) + ''\
                    + random.choice(second) + '' + random.choice(
            second_add) + '' + random.choice(third)
        bot.send_message(message.chat.id, horoskope)
    elif message.text.lower() == 'horoskope':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('дева', 'рыбы', 'весы', 'телец')
        keyboard.row('козерог', 'водолей', 'скорпион', 'овен')
        keyboard.row('стрелец', 'лев', 'рак', 'близнецы')
        keyboard.row('Августин', 'назад')
        bot.send_message(message.chat.id,
                         'выберите гороскоп', reply_markup=keyboard)
    elif message.text.lower() == 'auf':
        bot.send_sticker(message.chat.id,
                         'CAACAgIAAxkBAAPJX6Ansoqgy_1d'
                         '7vl7QkRojDDfgNcAAgIAA8qSuRtxcwqdq5TDwx4E')
        bot.send_message(message.chat.id, 'запустите аудио')
        bot.send_audio(message.chat.id,
                       'CQACAgIAAxkBAAIBI1-igdqQqploxnOpTA'
                       '8kkBiHb3jDAAJeCAACoH8AAUmUyi2tK13Y_h4E')
    elif message.text.lower() == 'назад':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row('horoskope', 'auf')
        bot.send_message(message.chat.id,
                         'выберите кнопку', reply_markup=keyboard)
    elif message.text.lower() == 'августин':
        bot.send_message(message.chat.id,
                         'Если вы нажали эту кнопку, значит '
                         'вам не повезло(ну или повезло)'
                         ' родиться Августином. К сожалению, если вы Августин,'
                         ' то никакой гороскоп вам не поможет.'
                         ' Единственное, что сделает'
                         ' ваш день удачным,'
                         ' так это купить шавуху своему близкому другу'
                         ' и создателю этого бота)')
    else:
        bot.send_message(message.chat.id, 'простите, я непонимаю вас')


bot.polling(none_stop=True)
