from . import window as w
from . import state as s
import random as r


def swim():
    """
    let your penguin go swimmingly swimming!!
    """
    def finish():
        w.main_window.add_text(f"{s.p.name} finished swimming!!!")
        salt_water_achieved = r.randint(3, 6)
        s.p.inventory["drinkables"]["salt water"] = s.p.inventory["drinkables"].get("salt water", 0) + salt_water_achieved
        w.main_window.add_text(f"while {s.p.name} was swimming, they got {salt_water_achieved}L of salt water, for a total of {s.p.inventory["drinkables"]["salt water"]}L!! 🎉🎉🧂")


    w.main_window.add_text(f"the {s.p.name} is going swimming!! 🏊🏊")
    w.main_window.after(r.randint(4000, 6000), finish)


w.main_window.keywords[
    "swim",
    "go-swim",
    "go-swimming",
    "pool-and-swim"
] = swim