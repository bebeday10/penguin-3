from . import window as w
from . import state as s
import random as r

def do_random(amount="1"):
    """
    Do a completely random thing. However, it cannot do dangerous things.
    """
    try: amount = int(amount)
    except ValueError: w.main_window.add_text("that isn't a number!!!"); return
    for _ in range(amount):
        w.main_window.add_text(f"{s.p.name} is going to do a random thing. beware.")
        random_thing = r.choice(list(w.main_window.keywords.values()))
        w.main_window.add_text(f"it is going to do {random_thing.__name__}.")
        if random_thing.__name__ == "exit_command":
            w.main_window.add_text("... but it couldn't because it was too dangerous. aww well.")
            return
        random_thing()

w.main_window.keywords[
    "do-random",
    "do-your-own",
    "random-do",
    "do-your-choice"
] = do_random