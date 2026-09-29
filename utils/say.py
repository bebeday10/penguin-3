from . import state as s
from . import window as w

def say(message=None, *messages):
    """
    make the penguin say something

    SKW:
        message (to talk): the message to talk about
    """
    if message is None:
        w.main_window.add_text("the penguin tries to say absolutely nothing but instead stayed entirely silent.")
        return

    message = " ".join([message, *messages])

    w.main_window.add_text(message)


w.main_window.keywords[
    "say",
    "say-message"
] = say