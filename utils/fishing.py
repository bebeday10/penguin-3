from . import window as w
from . import state as s
import random as r
import penglang.modules.pengfancywindow as pfw
from . import paths as p
import customtkinter as ctk
def fishing():
    """
    go fishing at the fishing platform with your penguin!
    """
    w.main_window.add_text("the penguin goes fishing at the fishing platform!! 🎣")
    def check():
        if current_side is None:
            w.main_window.add_text(f"{s.p.name} didn't choose in time...")
            fish_win.configure_widget("desc", text=f"{s.p.name} didn't choose in time...")
            return

        if side == current_side:
            w.main_window.add_text(f"congradulations! {s.p.name} earned the fish in time! 🎉🐟")
            fish_win.configure_widget("desc", text=f"congradulations! {s.p.name} earned the fish in time! 🎉🐟")
            s.p.inventory["edibles"]["fish"] = s.p.inventory["edibles"].get("fish", 0) + 1
            w.main_window.add_text(f"current amount of fish: {s.p.inventory["edibles"]["fish"]} 🐟")

        else:
            w.main_window.add_text(f"{s.p.name} chose the wrong side...")
            fish_win.configure_widget("desc", text=f"{s.p.name} chose the wrong side...")

        
    def countdown():
        nonlocal started, side
        if started:
            fish_win.configure_widget("desc", text="it already started!~")
            return
        started = True
        side = r.choice(sides)
        fish_win.configure_widget("desc", text=f"it starts! fish side: {side}")
        fish_win.after(5000, check)

    def input(button: str):
        nonlocal chosen, current_side, ended
        if not started:
            fish_win.configure_widget("desc", text="it hasn't started yet!")
        if ended:
            fish_win.configure_widget("desc", text="you already chose one or it's too late!")
        chosen = True
        ended = True
        current_side = button

    sides = [
        "right",
        "left",
        "center"
    ]
    side = None
    started = False
    ended = False
    chosen = False
    current_side = None
    fish_win = pfw.PenguinFancyWindow(window_title="fishing platform")
    fish_win.app_icon(p.PENGUIN_ICON)
    fish_win.add_widget(ctk.CTkLabel, "main label", 20, 20, "top", corner_radius=20, text="go fishing with the penguin!", font=("Roboto", 30, "bold"))
    fish_win.add_widget(ctk.CTkLabel, "desc", 10, 10, "top", text="the fish will appear as soon as you click start! after that, this text will say where it is. you have 5 seconds to click the button corresponding to it!")
    fish_win.add_frame("button frame", 20, 20, side="top")
    fish_win.add_button("start button", owner=fish_win.widgets["button frame"], command=countdown, text="start")
    for i in sides:
        fish_win.add_button(f"{i} button", command=lambda i=i: input(i), owner=fish_win.widgets["button frame"], text=f"{i}")
    fish_win.add_button("exit button", owner=fish_win.widgets["button frame"], command=fish_win.destroy, text="exit")
    fish_win.add_image("fishing platform", p.IMAGE_DIR / "fishing_platform.png", owner=fish_win.widgets["button frame"], image_size=(192, 192))


w.main_window.keywords[
    "fishing",
    "go-fishing",
    "acquire-fish-organically",
    "go-fish",
    "fish",
    "go-to-fishing-platform"
] = fishing
    
