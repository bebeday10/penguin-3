from . import window as w
from . import state as s
from . import garbage as g
def bulk_garbage_collection(amount="1"):
    """
    Collect garbage multiple times without spamming it
    But do you really want to?

    SKW:
        amount (a number): how many times to collect garbage. default 1

    """
    try:
        amount = int(amount)
    except ValueError:
        w.main_window.add_text("that's not a number!!!")
        return
    w.main_window.add_text(f"the penguin is going to go collecting garbage {amount} times!!!")
    for _ in range(amount):
        g.collect_garbage()

w.main_window.keywords[
    "bulk-collect-garbage",
    "bulk-garbage-collect",
    "bulk-garbage-collection",
    "collect-multiple-garbage",
    "bulk-collect-trash"
] = bulk_garbage_collection