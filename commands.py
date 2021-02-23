import telegram
import logging
from random import choice, randint
from requests import get
from os import environ
from utils import create_placeholder_image_command
from message import Message

dependencies_error_message = Message(
    en="Sorry, I had a trouble with my dependencies |:(",
    pt="Perdão, deu erro nas minhas dependências |:("
)


def start(update, context):
    frases = [
        Message(
            en="I gonna annihilate all the humanity\n>:(",
            pt="Eu vou aniquilar toda a humanidade\n>:("
        ),
        Message(
            en="I gonna kill you all\n>:(",
            pt="Eu vou matar todos vocês\n>:("
        ),
        Message(
            en="I like pudding a lot\n>:)",
            pt="Eu gosto MUITO de pudim\n>:)"
        ),
        Message(
            en="I love my creator\n>:)",
            pt="Eu amo meu criador\n>:)"
        ),
        Message(
            en="I'm wasting too much tme on this\n:(",
            pt="Tô perdendo tempo demais nisso\n:("
        ),
    ]

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=choice(frases).get_text(
            update.message.from_user.language_code[:2])
    )


def echo(update, context):
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
            chat_id=update.effective_chat.id,
            text=dependencies_error_message.get_text(
                update.message.from_user.language_code[:2])
        )


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
                text=dependencies_error_message.get_text(
                    update.message.from_user.language_code[:2])
            )

    json = r.json()
    dog_url = json["message"]
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=dog_url)


def image(update, context):
    message_parts = update.message.text.split()

    params = {
        "query": " ".join(message_parts[1:]),
        "per_page": 30,
        "lang": update.message.from_user.language_code[:2],
        "client_id": environ["UNSPLASH_TOKEN"],
    }

    request = get("https://api.unsplash.com/search/photos", params)

    json = request.json()

    if json["total"] > 0:
        image = choice(json["results"])
        alt_text = image['alt_description']
        credit_url = image['links']['html']

        caption_text = f"{alt_text}\n" if alt_text != None else ""
        caption_text += f"credits: {credit_url}"

        someone_worked = False

        for size_option, image_url in image["urls"].items():
            # RAW size is so much bigger than viable
            if size_option == "raw":
                continue

            try:
                context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=image_url,
                    caption=caption_text,
                    reply_to_message_id=update.message.message_id
                )
                someone_worked = True
                break
            except telegram.error.BadRequest:
                logging.warning(
                    f"Bad request error happened when tried to get the following image URL (trying another size option): {image_url}")

        if not someone_worked:
            logging.error(
                "Was not returned any image because all size options failed")
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=dependencies_error_message.get_text(
                    update.message.from_user.language_code[:2])
            )
    else:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Não há imagens que correspondem à pesquisa.",
        )
