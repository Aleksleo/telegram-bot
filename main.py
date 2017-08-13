# Telegram Bot Main file v0.1, Leonidov Aleksey

import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(211695408, "Hello, I'm your personal assistant")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello, I'm your personal assistant. How can I help you?")


"""
# Пока что не работает

@bot.message_handler(content_types=['commands'])
def handle_command(message):
    print("Пришла команда")
    if message.text == "/install":
        bot.send_message(message.chat.id, "`Type <b>/install</b> <i><package> <args></i>`")
"""

bot.polling(none_stop=True, interval=0)