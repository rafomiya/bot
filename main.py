from telegram import Bot

BOT_TOKEN = "1615739153:AAEO-cMX3e5aJClbqOVbOvXUkY3edOhcAxM"

bot = Bot(token=BOT_TOKEN)

bot_infos = bot.get_me()

print(bot_infos)
