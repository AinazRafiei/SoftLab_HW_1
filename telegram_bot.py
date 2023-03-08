# todo telegeram bot implement here

import os
import random
import logging
import telebot

TOKEN = '6261438264:AAHYs2yUmBmISRrMWQBKrTdmH-_1xARawyg'
URL = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id='

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "سلام!")

bot.infinity_polling()