from . import window as w
from . import state as s

def decorate_pumpkins(place="sidewalk"):
    """
    Decorate pumpkins
    place: put a place to decorate them
    """
    if not s.p.inventory["edibles"].get("pumpkin", 0):
        w.main_window.add_text("no pumpkins to decorate...")
        return

    s.p.inventory["edibles"]["pumpkin"] -= 1
    s.p.places.setdefault(place, {})
    s.p.places[place]["decorated pumpkins"] = s.p.places.get(place, {}).get("decorated pumpkins", 0) + 1

    w.main_window.add_text(f"pumpkins decorated! 🎃 current pumpkin amount: {s.p.inventory["edibles"]["pumpkin"]} pumpkins decorated at {place}: {s.p.places[place]["decorated pumpkins"]}")

w.main_window.keywords[
    "decorate-pumpkins",
    "pumpkin-decorate",
    "deco-pumpkins",
    "pumpkin-deco",
    "decorate-pumpkin",
    "pumpkins-decorate",
    "pumpkins-deco"
] = decorate_pumpkins

    