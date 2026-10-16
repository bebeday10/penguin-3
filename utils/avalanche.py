from . import window as w
from . import state as s

def avalanche():
    """
    check if there's an avalanche
    """
    w.main_window.add_text("good news: there's no avalanche.")
    w.main_window.add_text("...")
    w.main_window.add_text("or is there?")


w.main_window.keywords[
    "avalanche",
    "avalaunch",
    "avalanche-check",
    "check-avalanche",
    "freelance-avalanche-checking"
] = avalanche