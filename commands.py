from random import choice, randint
from requests import get

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


def bear(update, context):
    x = randint(300, 1000)
    y = randint(300, 1000)

    bear_url = f"https://placebear.com/{x}/{y}"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=bear_url)


def cage(update, context):
    x = randint(300, 1000)
    y = randint(300, 1000)

    cage_url = f"https://www.placecage.com/{x}/{y}"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=cage_url)


def bacon(update, context):
    x = randint(300, 1000)
    y = randint(300, 1000)

    bacon_url = f"https://baconmockup.com/{x}/{y}"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=bacon_url)


def cat(update, context):
    x = randint(300, 1000)
    y = randint(300, 1000)

    kitten_url = f"https://placekitten.com/{x}/{y}"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=kitten_url)


def dog(update, context):
    r = get("https://dog.ceo/api/breeds/image/random")
    if not r.ok:
        for _ in range(5):
            r = get("https://dog.ceo/api/breeds/image/random")
            if r.ok:
                break
        if not r.ok:
            context.bot.send_photo(chat_id=update.effective_chat.id, text="Perdão, deu erro em uma dependência :(")
    json = r.json()
    dog_url = json["message"]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_url)

