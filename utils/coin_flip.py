from . import window as w
from . import stats as s
import penglang.modules.pengrandom as pr
def coin_flip():
    """flip a coin."""
    side = pr.random_decision("heads", "tails")
    w.main_window.add_text(f"the coin landed on {side}!!")

w.main_window.keywords[
    "coin-flip",
    "flip-coin",
    "coin-toss",
    "coin-toggle"
] = coin_flip