from telegram import Bot
from os import environ
from read_env import read_env

read_env()

bot = Bot(token=environ["TELEGRAM_BOT_TOKEN"])

bot_infos = bot.get_me()

print(bot_infos)
