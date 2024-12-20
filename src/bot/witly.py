from time import sleep

import telebot
from telebot import types

from configs import tg_config, yandex_tmp_config

# Вставьте ваш Telegram API токен

# Создаем экземпляр бота
bot = telebot.TeleBot(tg_config.bot_token)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    web_app_url = f'https://oauth.yandex.ru/authorize?response_type=token&client_id={yandex_tmp_config.app_client_id}'
    web_app = types.WebAppInfo(web_app_url)
    button = types.InlineKeyboardButton(text='Открыть в Telegram', web_app=web_app)

    markup = types.InlineKeyboardMarkup()
    markup.add(button)

    bot.send_message(message.chat.id, "Нажмите на кнопку ниже, чтобы открыть веб-страницу в Telegram:",
                     reply_markup=markup)

