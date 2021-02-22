from random import randint

def get_random_dimension() -> tuple:
    """
    Returns an random dimension
    for placeholders.
    """
    x = randint(300, 1000)
    y = randint(300, 1000)

    return (x, y)

def create_placeholder_image_command(api_host: str):
    """
    Creates and returns an command
    handling function for image
    placeholders, given the api host
    URL.
    """
    def placeholder_command(update, context):
        x, y = get_random_dimension()

        api_url = f"{api_host}/{x}/{y}"
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=api_url)

    return placeholder_command
