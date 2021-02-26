import logging
from os import environ
from read_env import read_env
from updater import get_updater

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

read_env()
token = environ["TELEGRAM_BOT_TOKEN"]

updater = get_updater(token)

updater.start_polling()
updater.idle()
