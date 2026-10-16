from . import window as w
from . import state as s
import random as r
def processing_plant():
    """
    check on the big processing plant.
    """
    actions = [
        "processing air",
        "processing garbage",
        "sleeping",
        "malfunctioning",
        "collecting garbage",
        "processing life",
        "going home",
        "slacking off",
        "making a multi-media corporation",
        "processing taxes"
    ]
    w.main_window.add_text(f"the big processing plant is currently: {r.choice(actions)}")
    w.main_window.add_text(f"good thing: no one's taking {s.p.name}'s job 🐧")

w.main_window.keywords[
    "processing-plant",
    "check-processing-plant",
    "process-plant",
    "procplant"
] = processing_plant