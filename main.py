# Telegram Bot Main file v0.2, Leonidov Aleksey

import os

from bot.updater import Updater

def main():

    updater = Updater(os.environ['BOT_TOKEN'])

if __name__ == "__main__":
    main()
