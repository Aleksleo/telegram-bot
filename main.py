# Telegram Bot Main file v0.2, Leonidov Aleksey

import telebot
import constants
import messages
import psutil
import humanize


def main():

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
        answer = messages.text_messages['install'].format(replace_tag("<package> <args>"))
        bot.send_message(message.chat.id, answer, parse_mode="HTML")
        log(message, answer)

    @bot.message_handler(commands=['id'])
    def handle_text(message):
        if message.chat.type == "private":
            answer = messages.text_messages['chatid'].format(str(message.chat.id))
            bot.send_message(message.chat.id, answer, parse_mode="HTML")
            log(message, answer)
        elif message.chat.type == "group" or "supergroup":
            answer = messages.text_messages['groupid'].format(str(message.chat.id))
            bot.send_message(message.chat.id, answer, parse_mode="HTML")
            log(message, answer)

    @bot.message_handler(commands=['status'])
    def handle_text(message):
        answer = messages.text_messages['status'].format(
            psutil.cpu_percent(), psutil.cpu_count(),
            psutil.virtual_memory().percent,
            humanize.naturalsize(psutil.virtual_memory().total, binary=True, gnu=True))
        bot.send_message(message.chat.id, answer, parse_mode="HTML")
        log(message, answer)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        answer = "Hello, I'm your personal assistant. How can I help you?"
        if message.text == "Hello":
            bot.send_message(message.chat.id, answer, parse_mode="HTML")
            log(message, answer)

    bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
    main()
