"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import ephem

import local_settings

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)

# PROXY = {
#     'proxy_url': 'socks5://t1.learn.python.ru:1080',
#     'urllib3_proxy_kwargs': {
#         'username': 'learn',
#         'password': 'python'
#     }
# }

planet_list = [
    "Mars",
    "Venus",
    "Jupiter",
    "Uranus",
    "Mercury",
    "Neptune",
]


def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    text = user_text.split(" ")
    if len(text) == 2 and text[0] == "/planet" and text[1] in planet_list:
        dt_now = datetime.now().strftime("%Y/%m/%d")
        if text[1] == "Mars":
            planet = ephem.Mars(dt_now)
            const = ephem.constellation(planet)
        elif text[1] == "Venus":
            planet = ephem.Venus(dt_now)
            const = ephem.constellation(planet)
        elif text[1] == "Jupiter":
            planet = ephem.Jupiter(dt_now)
            const = ephem.constellation(planet)
        elif text[1] == "Uranus":
            planet = ephem.Uranus(dt_now)
            const = ephem.constellation(planet)
        elif text[1] == "Mercury":
            planet = ephem.Mercury(dt_now)
            const = ephem.constellation(planet)
        elif text[1] == "Neptune":
            planet = ephem.Neptune(dt_now)
            const = ephem.constellation(planet)
        answer = f"Планета {text[1]} сегодня находится в созвездии {const[1]}"
        update.message.reply_text(answer)
    else:
        update.message.reply_text(user_text)


def main():
    mybot = Updater(local_settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
