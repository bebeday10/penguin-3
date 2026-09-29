from . import state as s
from . import window as w

def eat(food_name=None):
    """
    eat food

    keywords:
        food_name (food in your inventory): food to eat
    """
    if food_name is None:
        w.main_window.add_text("the penguin cannot eat air... how to use eat: 'eat banana'")
        return

    if s.p.inventory["edibles"].get(food_name) is None:
        w.main_window.add_text("the penguin doesn't know how to eat that!!!")
        return

    if s.p.inventory["edibles"][food_name] <= 0:
        w.main_window.add_text("the penguin doesn't have any more of that food...")
        return

    s.p.inventory["edibles"][food_name] -= 1
    w.main_window.add_text(f"it feels refreshing to eat {food_name}! {food_name} left: {s.p.inventory["edibles"][food_name]}")

w.main_window.keywords[
    "eat",
    "eat-food",
    "food-eat",
    "devour"
] = eat
    