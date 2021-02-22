from random import choice


def start(update, context):
    frases = [
        "Eu vou aniquilar toda a humanidade >:(",
        "Eu vou matar todos vocês >:(",
        "Eu gosto MUITO de pudim >:)",
        "Eu gosto MUITO de pudim >:(",
        "Eu amo meu criador >:)",
        "Tô perdendo tempo demais nisso :(",
    ]

    context.bot.send_message(chat_id=update.effective_chat.id, text=choice(frases))


def echo(update, context):  # /echo abcdefghijklmnopqrtstuvwxyz
    answer = " ".join(update.message.text.split()[1:])
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


def total(update, context):
    nums_str = update.message.text.split()[1:]

    nums = map(float, nums_str)

    total = sum(nums)

    context.bot.send_message(chat_id=update.effective_chat.id, text=total)


def color(update, context):
    _, hexadecimal = update.message.text.split()
    color_url = f"https://via.placeholder.com/300/{hexadecimal}/{hexadecimal}"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=color_url)
