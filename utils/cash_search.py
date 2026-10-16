from . import window as w
from . import state as s
from . import penguin_func as pf
import random as r

def cash_search():
    """search for some cash. might work."""
    cashable = r.randint(1, 100)
    if cashable == 1:
        w.main_window.add_text("hm. turns out there is actually cash there.")
        drain = r.randint(1, 20)
        if drain == 1:
            w.main_window.add_text(f"... it dropped in the drain. unlucky {s.p.name}...")
            return

        s.p.cash += 20

        w.main_window.add_text(f"the {s.p.name} earned a fortune of $20!!! now it celebrates! 🎊")
        pf.penguin(5)
    else:
        w.main_window.add_text("what were we thinking?! of course there isn't any cash there!")

w.main_window.keywords[
    "cash-search",
    "search-cash",
    "find-fortune",
    "google-cash",
    "get-cash-by-going-to-the-road"
] = cash_search

