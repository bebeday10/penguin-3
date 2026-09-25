from . import window as w
from . import state as s

def hello():
    """say hello"""
    w.main_window.add_text(f"{s.p.name} says hello to you too! they're so happy to see you :D")

w.main_window.keywords[
    "hello",
    "say-hello",
    "greeting"
] = hello