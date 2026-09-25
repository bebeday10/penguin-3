from . import window as w
from . import state as s
from . import paths as p
import penglang.modules.pengfancywindow as pfw
import customtkinter as ctk

def change_name():
    """change your penguin's name at the name changing booth"""
    def change(_=None):
        new_name = name_window.get_entry("Name Entry")
        s.p.name = new_name 
        name_window.configure_widget("main name label", text=f"welcome to the name changing booth 🏷️ (your current name is {s.p.name})")
        name_window.remove_entry_text("Name Entry")

    name_window = pfw.PenguinFancyWindow(window_title="name changing booth")
    name_window.app_icon(p.IMAGE_DIR / "penguin_icon.png")
    name_window.add_widget(ctk.CTkLabel, "main name label", text=f"welcome to the name changing booth 🏷️ (your current name is {s.p.name})", font=("Roboto", 30, "bold"), side="top", x_space=25, y_space=25)
    name_window.add_frame("Name Frame", side="top", x_space=25, y_space=25)
    name_window.add_widget(ctk.CTkLabel, "desc", text="type to change your name", owner=name_window.widgets["Name Frame"], side="top", x_space=25, y_space=25)
    name_window.add_entry("Name Entry", placeholder_text="Enter a name here...", owner=name_window.widgets["Name Frame"], side="top", command=change, x_space=25, y_space=25, height=75)
    name_window.add_widget(ctk.CTkButton, "Exit", command=name_window.destroy, text="Exit the name changing booth", owner=name_window.widgets["Name Frame"], x_space=25, y_space=25, height=50)

w.main_window.keywords[
    "change-name",
    "swap-name",
    "name-change",
    "new-name"
] = change_name