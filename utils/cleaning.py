from . import window as w
from . import state as s
import random as r

def cleaning():
    """
    penguin cleans the ice floor! get some dirt.
    """
    def finish():
        w.main_window.add_text(f"after hard work, {s.p.name} finished cleaning!")
        dirt_earned = r.randint(3, 6)
        s.p.inventory["dirt"] = s.p.inventory.get("dirt", 0) + dirt_earned
        w.main_window.add_text(f"{s.p.name} earned {dirt_earned} dirts! 🎉🎉🎉🎉")
        

    w.main_window.add_text(f"the {s.p.name} goes cleaning! 🧹🧹")
    w.main_window.after(r.randint(2000, 4000), finish)

w.main_window.keywords[
    "clean",
    "cleaning",
    "go-clean",
    "go-cleaning",
    "clean-ice"
] = cleaning