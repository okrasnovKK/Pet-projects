import telebot, bot_db
from telebot import types


bot = telebot.TeleBot('XXX')
operator_id = 'XXX'
rescue_number = 112


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b> 👋'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    fire = types.KeyboardButton('Пожар 🔥')
    crash = types.KeyboardButton('ДТП 🚗')
    collapse = types.KeyboardButton('Обрушение 🏚️')
    offence = types.KeyboardButton('Правонарушение ⚖')
    ambulance = types.KeyboardButton('Нужна мед помощь 🩺')
    rescue = types.KeyboardButton('Нужна помощь спасателей 🚁')
    other = types.KeyboardButton('Другое 🔍')
    markup.add(fire, crash, collapse, offence, ambulance, rescue, other)
    mess_2 = 'Пожалуйста, выберите из меню тему Вашего обращения👇 \n' \
                '⚠️Обращаем Ваше внимание о недопущении подачи заведомо ложных сообщений⛔'
    bot.send_message(message.chat.id, mess_2, reply_markup=markup)
    add_db(message.from_user.id, message.text)


@bot.message_handler(content_types=['text'])
def get_user_message(message):
    if message.text in ['Пожар 🔥', 'ДТП 🚗', 'Обрушение 🏚️', 'Правонарушение ⚖', 'Нужна мед помощь 🩺', 'Нужна помощь спасателей 🚁']:
        mess = 'Отправьте геолокацию на карте 📍' \
               ' или тектовым сообщением адрес места происшествия (населённый пункт, улица, номер дома, корпуса и т.д.) ' \
               'или иные сведения о месте происшествия 📝'
        bot.send_message(message.chat.id, mess)
        mess_2 = f'Cообщение от [{message.from_user.id}](tg://user?id={message.from_user.id}): {message.text}'
        bot.send_message(operator_id, mess_2, parse_mode='Markdown')
        add_db(message.from_user.id, message.text)
    elif message.text in ['Другое 🔍']:
        mess = 'Здесь сделать кнопки в зависимости от возможностей: эвакуатор, совет'
        bot.send_message(message.chat.id, mess)
        add_db(message.from_user.id, message.text)
    elif len(message.text) > 5:
        mess = 'Обработка информации ⏱️ \nОтправьте в сообщении информацию о наличии ' \
                'опасности людям и иные имеющиеся сведения 📝' \
                'Также, при возможности, отправьте, пожалуйста, фото или короткое видео с места происшествия 📸📹' \
                '\nЭто очень поможет нам! 🙏'
        bot.send_message(message.chat.id, mess)
        mess_2 = f'Cообщение от [{message.from_user.id}](tg://user?id={message.from_user.id}): {message.text}'
        bot.send_message(operator_id, mess_2, parse_mode='Markdown')
        add_db(message.from_user.id, message.text)
    else:
        bot.send_message(message.chat.id, '❗ Пожалуйста, попробуйте заново.')
        add_db(message.from_user.id, message.text)


@bot.message_handler(content_types=['location'])
def get_user_location(message):
    bot.send_message(message.chat.id, 'Обработка информации ⏱️ \nОтправьте в сообщении информацию о наличии ' \
                                      'опасности людям и иные имеющиеся сведения 📝 ' \
                                      'Также, при возможности, отправьте, пожалуйста, фото или короткое видео с места происшествия 📸📹' \
                                      '\nЭто очень поможет нам! 🙏')
    # mess_2 = f'Cообщение от "{message.from_user.id}":'
    mess_2 = f'Cообщение от [{message.from_user.id}](tg://user?id={message.from_user.id}): '
    bot.send_message(operator_id, mess_2, parse_mode='Markdown')
    bot.send_location(operator_id, message.location.latitude, message.location.longitude)
    add_db(message.from_user.id, [message.location.latitude, message.location.longitude])


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Спасибо за отправленную информацию 👍 Идёт её обработка ⏱️ \n' \
                                          'Если у Вас появятся дополнительные сведения просим сообщить их также здесь ' \
                                          f'или по номеру телефона "{rescue_number}"  ☎️\n ' \
                                          '\nЭто очень поможет нам! 🙏')
    mess_2 = f'Cообщение от [{message.from_user.id}](tg://user?id={message.from_user.id}): '
    bot.send_message(operator_id, mess_2, parse_mode='Markdown')
    bot.send_photo(operator_id, message.photo[1].file_id)
    add_db(message.from_user.id, message.photo[1].file_id)


def add_db(info_1, info_2):
    bot_db.add(info_1, info_2)



bot.polling(none_stop=True)