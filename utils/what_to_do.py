from . import window as w
from . import state as s
import random as r

def what_do():
    """ask the penguin what to do!!"""
    w.main_window.add_text(f"{s.p.name} thinks {r.choice(list(w.main_window.keywords.keys()))} is a good keyword to try out!! ooh ooh!")

w.main_window.keywords[
    "what-to-do",
    "what-should-i-do",
    "do-what",
    "what-do-you-think-i-should-do",
    "what-do"
] = what_do