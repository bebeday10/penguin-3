from . import window as w
from . import state as s
from . import paths as p
from . import penguin_func as pf
import penglang.modules.pengfancywindow as pfw
import customtkinter as ctk

def grocery():
    """
    buy an item at the grocery for your penguin to eat!!
    """
    def sale(item, price):
        if price > s.p.cash:
            grocery_window.configure_widget("desc", text="the penguin doesn't have that much money...")
            return

        s.p.cash -= price
        s.p.inventory["edibles"][item] = s.p.inventory["edibles"].get(item, 0) + 1
        w.main_window.add_text(f"the penguin is very happy that they got a {item}!! ooh ooh!!! 🎉🐧")
        grocery_window.configure_widget("store label", text=f"the grocery with food ({s.p.name} currently has ${s.p.cash:.2f})")
        pf.penguin(3)

    grocery_window = pfw.PenguinFancyWindow(window_title="the grocery of penguin", size="1500x900")
    grocery_window.app_icon(p.PENGUIN_ICON)

    grocery_window.add_widget(ctk.CTkLabel, "store label", 25, 25, side="left", text=f"the grocery with food ({s.p.name} currently has ${s.p.cash:.2f})", font=("Roboto", 30, "bold"))
    grocery_items = {
        "banana": 2.5,
        "fish": 10,
        "peanuts": 0.5,
        "bread": 4.25,
        "potato": 3.49,
        "mushroom": 1.2,
        "watermelon": 23.65
    }
    grocery_window.add_widget(ctk.CTkScrollableFrame, "Grocery Frame", 25, 25, side="left")
    grocery_window.add_widget(ctk.CTkLabel, "desc", 25, 25, "top", grocery_window.widgets["Grocery Frame"], text="click something to buy it", height=50)
    for item, price in grocery_items.items():
        grocery_window.add_widget(ctk.CTkButton, f"{item}_button", command=lambda item=item, price=price: sale(item, price), side="top", text=f"{item} (${price})", owner=grocery_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)

    grocery_window.add_widget(ctk.CTkButton, "exit button", command=grocery_window.destroy, side="top", text="Exit the grocery", owner=grocery_window.widgets["Grocery Frame"], height=60, x_space=25, y_space=25)

w.main_window.keywords[
    "grocery",
    "go-to-grocery",
    "groceries"
] = grocery



