from . import state as s
from . import window as w

def drink(drink_name: str = None, *space_drinks: str):
    """
    drink something

    keywords:
        drink_name (drink in your inventory): drink to drink
    """
    
    if drink_name is None:
        w.main_window.add_text("the penguin cannot drink air... how to use drink: 'drink salt water'")
        return
    full_drink_name = " ".join([drink_name, *space_drinks])
    if s.p.inventory["drinkables"].get(full_drink_name) is None:
        w.main_window.add_text("the penguin doesn't know how to drink that!!!")
        return

    if s.p.inventory["drinkables"][full_drink_name] <= 0:
        w.main_window.add_text("the penguin doesn't have any more of that drink...")
        return

    s.p.inventory["drinkables"][full_drink_name] -= 1
    w.main_window.add_text(f"it feels refreshing to drink {full_drink_name}! {full_drink_name} left: {s.p.inventory["drinkables"][full_drink_name]}")

w.main_window.keywords[
    "drink",
    "drink-drink",
    "drink-a-drink",
    "guzzle",
    "quaff"
] = drink
    