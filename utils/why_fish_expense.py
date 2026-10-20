from . import state as s
from . import window as w

def why_are_fish_expensive():
    """
    ask why fish are expensive.
    """
    w.main_window.add_text(f"{s.p.name} thinks fish are expensive ($10) because penguins should learn how to fish themselves for free.")


w.main_window.keywords[
    "why-are-fish-expensive",
    "fish-why-$",
    "fish-$$$",
    "fish-expensive"
] = why_are_fish_expensive