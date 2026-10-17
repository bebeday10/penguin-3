from . import window as w
from . import state as s
import random as r

def country_wants():
    """
    check the amount of countries that want the penguin.
    """
    w.main_window.add_text(f"{s.p.name} is wanted in: {r.randint(0, 195)} countries.")


w.main_window.keywords[
    "check-countries-that-want",
    "country-wants",
    "penguin-wanted-countries"
] = country_wants