from . import window as w
from . import state as s

def dance(dance_style="penguin"):
    """
    do a cool dance!!!

    Subkeywords:
        dance_style: after 'dance', type out the dance style!! defaults to "penguin".
    """
    w.main_window.add_text(f"penguin does a {dance_style} dance!!! ooh ooh! 🪩")

w.main_window.keywords[
    "dance",
    "do-a-dance"
] = dance