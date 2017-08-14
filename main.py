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

# Less- or greater-than sign replacement function

def replace_tag(value):
    return value.replace('<', "&lt;").replace('>', "&gt;")

@bot.message_handler(commands=['install'])
def handle_text(message):
    answer = "/install <b>" + replace_tag("<package> <args>") + "</b>"
    answer += "\n\n<code>Packages:\n linux middleware release\n linux middleware beta</code>"
    bot.send_message(message.chat.id, answer, parse_mode="HTML")
    log(message, answer)

@bot.message_handler(commands=['id'])
def handle_text(message):
    if message.chat.type == "private":
        answer = "Your chat ID: <b>" + str(message.chat.id) + "</b>"
        bot.send_message(message.chat.id, answer, parse_mode="HTML")
    elif message.chat.type == "group" or "supergroup":
        answer = "Group ID: <b>" + str(message.chat.id) + "</b>"
        bot.send_message(message.chat.id, answer, parse_mode="HTML")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Hello, I'm your personal assistant. How can I help you?"
    if message.text == "Hello":
        bot.send_message(message.chat.id, answer, parse_mode="HTML")
        log(message, answer)

bot.polling(none_stop=True, interval=0)