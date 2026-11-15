from . import window as w
from . import state as s

from random import randint
def instant_bulk_garbage_collection(amount="1"):
    """
    Collect garbage instantly multiple times without spamming it
    But do you really want to?

    SKW:
        amount (a number): how many times to collect garbage. default 1

    """
    try:
        amount = int(amount)
    except ValueError:
        w.main_window.add_text("that's not a number!!!")
        return
    def finish_garbage_collection():
        earned: int = randint(3, 6) * amount
        s.p.garbage += earned
        w.main_window.add_text(f"{s.p.name} collected {earned} kg and now has {s.p.garbage} kg of garbage!!!")
    w.main_window.add_text(f"{s.p.name} is collecting garbage...")

    w.manager.wait(randint(2000, 5000), finish_garbage_collection)

w.main_window.keywords[
    "instant-bulk-collect-garbage",
    "instant-bulk-garbage-collect",
    "instant-bulk-garbage-collection",
    "instant-collect-multiple-garbage",
    "instant-bulk-collect-trash"
] = instant_bulk_garbage_collection