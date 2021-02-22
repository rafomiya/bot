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
