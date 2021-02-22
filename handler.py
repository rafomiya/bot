from telegram.ext import Dispatcher, CommandHandler
from commands import *


class Handler:
    def __init__(self, dispatcher: Dispatcher):
        self.dispatcher = dispatcher

    def set_command_handler(self, command: str, handling_function):
        """
        Set the command handler to dispatcher.
        """
        command_handler = CommandHandler(command, handling_function)
        self.dispatcher.add_handler(command_handler)

    def add_handlers(self):
        """
        Add all the handlers to the bot.
        """
        self.set_command_handler("start", start)
        self.set_command_handler("echo", echo)
        self.set_command_handler("total", total)
