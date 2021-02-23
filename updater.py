from telegram.ext import Updater
from handler import Handler


def get_updater(token: str) -> Updater:
    """
    Returns a instancied updater
    object given the bot token.
    """
    updater = Updater(token, use_context=True)

    handler = Handler(updater.dispatcher)
    handler.add_handlers()

    return updater
