from . import window as w
from . import state as s

def stats():
    """show the stats of your penguin!!! useful to check if you have stuff."""
    w.main_window.add_text(f"--- {s.p.name}'s stats ---")
    for k, v in s.p.__dict__.items():
        w.main_window.add_text(f"{k}: {v}")

w.main_window.keywords[
    "stats",
    "see-stats"
] = stats