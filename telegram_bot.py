import telebot

print("bot started")
TOKEN = '6261438264:AAHYs2yUmBmISRrMWQBKrTdmH-_1xARawyg'
URL = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id='

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام!"
                          "\n چطور میتونم به شما کمک کنم؟")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "هر چیزی که میخوای تایپ کن!")


@bot.message_handler(commands=['intro'])
def send_help(message):
    bot.send_message(message.chat.id, "این بات تمرین اول آز نرم هست")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == "تاس":
        bot.send_dice(message.chat.id)
    else: bot.reply_to(message, message.text)


print("bot is polling")
bot.infinity_polling()
