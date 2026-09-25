from . import window as w
from . import state as s
import random as r

def penguin(amount=5):
    """
    say penguin stuff.

    Sub Keywords:
        amount: after "penguin", put a number. without it, it defaults to 5.
    """
    try: amount = int(amount)
    except ValueError: w.main_window.add_text("that's not a number!!!"); return
    def logic():
        w.main_window.add_text(f"ooh {r.randint(1, 100)} {s.p.name}!! 🐧")
    for _ in range(amount):
        w.manager.update()
        w.manager.after(r.randint(100, 500), logic)

w.main_window.keywords[
    "penguin"
] = penguin
        