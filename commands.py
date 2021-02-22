from random import choice, randint
from requests import get
<<<<<<< HEAD
from os import environ
from urllib.parse import quote_plus

=======
from utils import create_placeholder_image_command
>>>>>>> 7ab9b82ebaf1677eba064360f2ea9640a251cb64

def start(update, context):
    frases = [
        "Eu vou aniquilar toda a humanidade\n>:(",
        "Eu vou matar todos vocês\n>:(",
        "Eu gosto MUITO de pudim\n>:)",
        "Eu gosto MUITO de pudim\n>:(",
        "Eu amo meu criador\n>:)",
        "Tô perdendo tempo demais nisso\n:(",
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
                chat_id=update.effective_chat.id,
                text="Perdão, deu erro em uma dependência :(",
            )
    json = r.json()
    dog_url = json["message"]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_url)
<<<<<<< HEAD


def image(update, context):
    complete_message = update.message.text.split()
    search = quote_plus(" ".join(complete_message[1:]))
    unsplash_token = environ["UNSPLASH_TOKEN"]
    request = get(
        f"https://api.unsplash.com//search/photos/?query={search}&per_page=30&page=5&client_id={unsplash_token}"
    )

    json = request.json()
    if json["total"] == 0:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Não há imagens que correspondem à pesquisa.",
        )
    else:
        image = choice(json["results"])
        if image["alt_description"] != None:
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=image["urls"]["full"],
                caption=f"{image['alt_description']}\ncredits: {image['links']['html']}",
            )
        else:
            context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=image["urls"]["full"],
                caption=f"credits: {image['links']['html']}",
            )
=======
>>>>>>> 7ab9b82ebaf1677eba064360f2ea9640a251cb64
