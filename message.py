class Message:
    """
    Message is used to build a message
    with language options.
    """

    __idioms_and_texts = dict()

    def __init__(self, **kwargs):
        if "en" not in kwargs.keys():
            raise Exception(
                "The 'en' language code must be specified on a Message constructor")

        for language_code, text in kwargs.items():
            self.__idioms_and_texts[language_code] = text

    def get_text(self, lang: str = "en"):
        """
        Returns the message text given
        the language code. If the code
        was not specified, it returns
        the message with "en" code.
        """
        text = self.__idioms_and_texts[lang]

        return text if text != None else self.__idioms_and_texts["en"]
