from . import state as s
from . import window as w
from . import paths as p
from random import randint, uniform
import penglang.modules.pengfancywindow as pfw
import customtkinter as ctk
def collect_garbage():
    """
    collect some garbage for the penguins
    """
    def finish_garbage_collection():
        earned: int = randint(3, 6)
        s.p.garbage += earned
        w.main_window.add_text(f"{s.p.name} collected {earned} kg and now has {s.p.garbage} kg of garbage!!!")
    w.main_window.add_text(f"{s.p.name} is collecting garbage...")

    w.manager.wait(randint(2000, 5000), finish_garbage_collection)

def sell_garbage():
    """
    sell garbage for money (easy money)
    """
    def complete_sell(_=None):
        entered = sell_window.get_entry("Sell entry")
        sell_window.remove_entry_text("Sell entry")
        try:
            entered = int(entered)
        except ValueError:
            sell_window.configure_widget("desc", text="that's not a full number!!!")
            return

        if entered <= 0:
            sell_window.configure_widget("desc", text="that's 0 or below...")
        elif entered > s.p.garbage:
            sell_window.configure_widget("desc", text=f"{s.p.name} doesn't have enough garbage!!!")
        else:
            s.p.garbage -= entered
            earnings_now = entered * uniform(0.5, 2.0)
            s.p.cash += earnings_now
            sell_window.configure_widget("desc", text=f"{s.p.name} sold {entered} kg and earned ${earnings_now:.2f}!!")
            sell_window.configure_widget("main label", text=f"sell some garbage ({s.p.name} has {s.p.garbage}kg of it)")
            w.main_window.add_text(f"the {s.p.name} celebrates! ooh ooh!!! 🐧🍌🎉🎉")
            

    sell_window = pfw.PenguinFancyWindow(window_title="sell garbage")
    sell_window.app_icon(p.IMAGE_DIR / "penguin_icon.png")
    sell_window.add_widget(ctk.CTkLabel, "main label", text=f"sell some garbage ({s.p.name} has {s.p.garbage}kg of it)", font=("Roboto", 30, "bold"), side="top", x_space=25, y_space=25)
    sell_window.add_frame("Entry Frame", side="top", x_space=25, y_space=25)
    sell_window.add_widget(ctk.CTkLabel, "desc", text="type a number of kg to sell...", owner=sell_window.widgets["Entry Frame"], side="top", y_space=20, x_space=20)
    sell_window.add_entry("Sell entry", placeholder_text="Type a number, like 3...", owner=sell_window.widgets["Entry Frame"], side="left", y_space=20, x_space=20, command=complete_sell)
    sell_window.configure_widget("Sell entry", width=300)
    sell_window.add_image("garbage_sell_image", p.IMAGE_DIR / "garbage_selling.png", owner=sell_window.widgets["Entry Frame"])
    

w.main_window.keywords[
    "collect-garbage",
    "start-garbage-collection",
    "earn-garbage"
] = collect_garbage
w.main_window.keywords[
    "sell-garbage",
    "start-selling-garbage",
    "sellgarbage"
] = sell_garbage