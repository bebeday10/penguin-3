from . import state as s
from . import window as w
from random import randint
def collect_garbage():
    """
    collect some garbage for the penguins
    """
    def finish_garbage_collection():
        earned: int = randint(3, 6)
        s.p.garbage += earned
        w.main_window.add_text(f"{s.p.name} collected {earned} kg and now has {s.p.garbage} kg of garbage!!!")
    w.main_window.add_text(f"{s.p.name} is collecting garbage...")

    w.manager.wait(randint(2000, 5000), finish_garbage_collection)

w.main_window.keywords[
    "collect-garbage",
    "start-garbage-collection",
    "earn-garbage"
] = collect_garbage