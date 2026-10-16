from . import window as w
from . import state as s
from . import paths as p
from . import penguin_func as pf
import penglang.modules.pengfancywindow as pfw
import customtkinter as ctk

def fish_market():
    """
    buy deluxe fish at the fish market for great fish
    """
    w.main_window.add_text(f"{s.p.name} goes to the fish market!!!")
    def sale(item, price):
        if price > s.p.cash:
            market_window.configure_widget("desc", text="the penguin doesn't have that much money...")
            w.main_window.add_text(f"{s.p.name} didn't have any more money to buy {item}... it was ${price - s.p.cash:.2f} too much...")
            return

        s.p.cash -= price
        s.p.inventory["edibles"][item] = s.p.inventory["edibles"].get(item, 0) + 1
        w.main_window.add_text(f"the penguin is very happy that they got a {item} (${price})!! ooh ooh!!! 🎉🐧")
        market_window.configure_widget("store label", text=f"the market with fish ({s.p.name} currently has ${s.p.cash:.2f})")
        pf.penguin(3)

    market_window = pfw.PenguinFancyWindow(window_title="the market of fish", size="1500x900")
    market_window.app_icon(p.PENGUIN_ICON)

    market_window.add_widget(ctk.CTkLabel, "store label", 25, 25, side="left", text=f"the market with fish ({s.p.name} currently has ${s.p.cash:.2f})", font=("Roboto", 30, "bold"))
    fishes = {
        "fish": 10.0,
        "gold fish": 45.50,
        "carp": 15.25,
        "long fish": 20.50,
        "economy fish": 5.0,
        "rich fish": 50.10,
        "tuna": 32.16,
        "cod": 11.23,
        "salmon": 34.5,
        "sashimi": 150.78,
    }
    market_window.add_widget(ctk.CTkScrollableFrame, "Grocery Frame", 25, 25, side="left")
    market_window.add_widget(ctk.CTkLabel, "desc", 25, 25, "top", market_window.widgets["Grocery Frame"], text="click something to buy it", height=50)
    for item, price in fishes.items():
        market_window.add_widget(ctk.CTkButton, f"{item}_button", command=lambda item=item, price=price: sale(item, price), side="top", text=f"{item} (${price})", owner=market_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)

    market_window.add_widget(ctk.CTkButton, "exit button", command=market_window.destroy, side="top", text="Exit the fish market", owner=market_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)

w.main_window.keywords[
    "buy-fish",
    "go-to-fish-market",
    "fish-market",
    "fish-buy-area",
    "in-need-of-fish"
] = fish_market



