def int_func(text):
    """
    :param text: a lowercase and contained only latin letters
    :return: every word with a capital letter
    """
    if text.islower() and text.isascii():
        return text.title()
    else:
        return "Text should be a lowercase and contained only latin letters"


print(int_func("text in a lowercase and contain only latin letters"))
