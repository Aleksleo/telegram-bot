# Telegram Bot Main file v0.1, Leonidov Aleksey

import telebot
import constants

bot = telebot.TeleBot(constants.token)

# Logging into console
print(bot.get_me())

def log(message, answer):
    print("\n --------------")
    from datetime import datetime
    print(datetime.now())
    print("Message from {0} {1}. (id = {2}) \n Text: {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)


@bot.message_handler(commands=['install'])
def handle_text(message):
    answer = """Type 
    /install <package> <args>"""
    bot.send_message(message.chat.id, answer)
    log(message, answer)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Hello, I'm your personal assistant. How can I help you?"
    if message.text == "Hello":
        bot.send_message(message.chat.id, answer)
        log(message,answer)

bot.polling(none_stop=True, interval=0)