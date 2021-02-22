from telegram import Bot
from telegram.ext import Updater, CommandHandler
from os import environ
from read_env import read_env
from random import choice

frases = [
    "Eu vou aniquilar toda a humanidade >:(",
    "Eu vou matar todos vocês >:(",
    "Eu gosto MUITO de pudim >:)",
    "Eu gosto MUITO de pudim >:(",
    "Eu amo meu criador >:)",
    "Tô perdendo tempo demais nisso :(",
]

read_env()

bot = Bot(token=environ["TELEGRAM_BOT_TOKEN"])
token = environ["TELEGRAM_BOT_TOKEN"]

read_env()

bot = Bot(token=token)

bot_infos = bot.get_me()

# print(bot_infos)

"""
Tarefa 1 da noite:
    Fazer o bot responer "Estou vivo" quando alguém der /start.
"""


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=choice(frases))


updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler(
    "start", start
)  # esse segundo parâmetro 'start' se refere à função definida anteriormente na linha 27
dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()