from . import window as w
from . import state as s
import random as r
from . import cash_search as cs
from . import news as n
from . import garbage as g

def random_event_loop():

    chance = lambda: r.uniform(0, 100000)

    if chance() <= 10:
        w.main_window.add_text(f"lucky {s.p.name}! they found 10 cents!")
        s.p.cash += 0.1

    if chance() <= 30:
        w.main_window.add_text("it seems to be raining. expect water drops.")

    if chance() <= 0.25:
        w.main_window.add_text(f"{s.p.name} found a banana on the sidewalk!")
        s.p.inventory["edibles"]["banana"] = s.p.inventory["edibles"].get("banana", 0) + 1

    if chance() <= 40:
        w.main_window.add_text("it seems to be cooling outside. maybe go for some groceries?")

    if chance() <= 30:
        w.main_window.add_text("the sun has appeared.")

    if chance() <= 30:
        w.main_window.add_text(f"the {s.p.name} feels like collecting garbage right now.")

    if chance() <= 9:
        w.main_window.add_text("the penguin decides to search for cash as free time.")
        cs.cash_search()

    if chance() <= 60 and s.p.garbage == 0:
        w.main_window.add_text(f"{s.p.name} seems to have zero (0) kg of garbage. consider collecting garbage?")

    if chance() <= 30:
        w.main_window.add_text("it is getting cloudy.")

    if chance() <= 6:
        w.main_window.add_text("the penguin decides to read some news.")
        n.news()

    if chance() <= 8:
        w.main_window.add_text("the penguin is going to collect garbage without anyone's consent.")
        g.collect_garbage()

    if chance() <= 5:
        w.main_window.add_text("the penguin slipped off the ice rink. they want food now.")

    if chance() <= 20:
        w.main_window.add_text("the penguin yearns for sashimi. maybe you should go to the fish market?")


    w.main_window.after(50, random_event_loop)