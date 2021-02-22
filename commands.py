from random import choice, randint
from requests import get
from utils import create_placeholder_image_command


def start(update, context):
    frases = [
        "Eu vou aniquilar toda a humanidade >:(",
        "Eu vou matar todos vocês >:(",
        "Eu gosto MUITO de pudim >:)",
        "Eu gosto MUITO de pudim >:(",
        "Eu amo meu criador >:)",
        "Tô perdendo tempo demais nisso :(",
    ]

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=choice(frases))


def echo(update, context):  # /echo abcdefghijklmnopqrtstuvwxyz
    answer = " ".join(update.message.text.split()[1:])
    context.bot.send_message(chat_id=update.effective_chat.id, text=answer)


def total(update, context):
    nums_str = update.message.text.split()[1:]

    nums = map(float, nums_str)

    total = sum(nums)

    context.bot.send_message(chat_id=update.effective_chat.id, text=total)


def color(update, context):
    resolution = 300
    _, hex_color = update.message.text.split()

    apis_options = [
        "https://via.placeholder.com",
        "https://dummyimage.com",
        "https://fakeimg.pl"
    ]

    someone_worked = False

    for option in apis_options:
        color_url = f"{option}/{resolution}/{hex_color}/{hex_color}"

        if get(color_url).ok:
            """
            If the service is up and running
            properly, use it.
            """
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=color_url)
            someone_worked = True
            break

    if not someone_worked:
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="I had a trouble with my dependencies |:(")


bear = create_placeholder_image_command("https://placebear.com")
cage = create_placeholder_image_command("https://www.placecage.com")
bacon = create_placeholder_image_command("https://baconmockup.com")
cat = create_placeholder_image_command("https://placekitten.com")


def dog(update, context):
    r = get("https://dog.ceo/api/breeds/image/random")
    if not r.ok:
        for _ in range(5):
            r = get("https://dog.ceo/api/breeds/image/random")
            if r.ok:
                break
        if not r.ok:
            context.bot.send_photo(
                chat_id=update.effective_chat.id, text="Perdão, deu erro em uma dependência :(")
    json = r.json()
    dog_url = json["message"]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_url)
