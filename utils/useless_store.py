from . import window as w
from . import state as s
from . import paths as p
from . import penguin_func as pf
import penglang.modules.pengfancywindow as pfw
import customtkinter as ctk

def jimmy_jenguin_store():
    """
    buy unneeded items at the jimmy jenguin luxury store
    """
    w.main_window.add_text(f"{s.p.name} goes to the jimmy jenguin luxury store!!!")
    def sale(item, price):
        if price > s.p.cash:
            market_window.configure_widget("desc", text="the penguin doesn't have that much money...")
            w.main_window.add_text(f"{s.p.name} didn't have any more money to buy {item}... it was ${price - s.p.cash:.2f} too much...")
            return

        s.p.cash -= price
        s.p.inventory[item] = s.p.inventory.get(item, 0) + 1
        w.main_window.add_text(f"the penguin is very happy that they got a {item} (${price})!! ooh ooh!!! 🎉🐧")
        market_window.configure_widget("store label", text=f"the jimmy jenguin luxury store ({s.p.name} currently has ${s.p.cash:.2f})")
        pf.penguin(3)

    market_window = pfw.PenguinFancyWindow(window_title="the jimmy jenguin luxury store", size="1500x900")
    market_window.app_icon(p.PENGUIN_ICON)

    market_window.add_widget(ctk.CTkLabel, "store label", 25, 25, side="left", text=f"the jimmy jenguin luxury store ({s.p.name} currently has ${s.p.cash:.2f})", font=("Roboto", 30, "bold"))
    luxuries = {
        "Jimmy Jenguin's signed photograph": 100_000,
        "Jimmy Jenguin statue": 499_999.99,
        "Umbrella Gold": 10_000,
        "Ice flake personally handled by Jimmy Jenguin": 1_000_000,
        "Crystal": 75_000,
        "Jimmy Jenguin 1:1 replica": 10_000_000 
    }
    market_window.add_widget(ctk.CTkScrollableFrame, "Grocery Frame", 25, 25, side="left")
    market_window.add_widget(ctk.CTkLabel, "desc", 25, 25, "top", market_window.widgets["Grocery Frame"], text="click something to buy it", height=50)
    for item, price in luxuries.items():
        market_window.add_widget(ctk.CTkButton, f"{item}_button", command=lambda item=item, price=price: sale(item, price), side="top", text=f"{item} (${price})", owner=market_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)

    market_window.add_widget(ctk.CTkButton, "exit button", command=market_window.destroy, side="top", text="Exit the jimmy jenguin luxury store", owner=market_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)



w.main_window.keywords[
    "jimmy-jenguin-store",
    "luxury-store",
    "in-need-of-luxury",
    "jimmy-jenguin-luxury-store",
    "the-jimmy-jenguin-luxury-store"
] = jimmy_jenguin_store