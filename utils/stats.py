from . import window as w
from . import state as s

def stats():
    """show the stats of your penguin!!! useful to check if you have stuff."""
    def auto_format(k, v):
        if isinstance(v, dict):
            w.main_window.add_text(f"{k}:")
            w.main_window.add_text("------")
            for sub_k, sub_v in v.items():
                auto_format(sub_k, sub_v)
            w.main_window.add_text("------")
        elif isinstance(v, (list, tuple, set)):
            w.main_window.add_text(f"{k}:")
            w.main_window.add_text("------")
            for i, sub_item in enumerate(v):
                auto_format(i ,sub_item)
        else:
            w.main_window.add_text(f"{k}: {v}")

    w.main_window.add_text(f"--- {s.p.name}'s stats ---")
    for k, v in s.p.__dict__.items():
        auto_format(k, v)

w.main_window.keywords[
    "stats",
    "see-stats"
] = stats