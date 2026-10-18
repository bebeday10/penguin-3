from . import window as w
from . import state as s

def dirt_something(thing=None, *things):
    """
    dirt a thing

    SKW:
        thing: thing to dirt
    """
    if s.p.inventory.get("dirt", 0) == 0:
        w.main_window.add_text(f"{s.p.name} has no dirt to dirt...")
        return
    if thing is None:
        w.main_window.add_text("the penguin dirts nothing!")
        s.p.inventory["dirt"] -= 1
        return

    thing = " ".join([thing, *things])

    w.main_window.add_text(f"the penguin dirts the {thing}!")
    s.p.inventory["dirt"] -= 1

w.main_window.keywords[
    "dirt",
    "dirt-the",
    "dirt-something"
] = dirt_something