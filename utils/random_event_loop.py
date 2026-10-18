from . import window as w
from . import state as s
import random as r
from . import cash_search as cs
from . import news as n
from . import garbage as g
from . import store as st
from . import fish_market as fm
from . import fishing
from . import what_to_do as wtd
from . import eat
from . import cleaning as c

def random_event_loop():

    chance = lambda: r.uniform(0, 140000)

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

    if chance() <= 40 and s.p.garbage == 0:
        w.main_window.add_text(f"{s.p.name} seems to have zero (0) kg of garbage. consider collecting garbage?")

    if chance() <= 30:
        w.main_window.add_text("it is getting cloudy.")

    if chance() <= 6:
        w.main_window.add_text("the penguin decides to read some news.")
        n.news()

    if chance() <= 8:
        w.main_window.add_text("the penguin is going to collect garbage without anyone's consent.")
        g.collect_garbage()

    if chance() <= 7:
        w.main_window.add_text(f"{s.p.name} is going to go cleaning without anyone's consent. it looked pretty dirty.")
        c.cleaning()

    if chance() <= 5:
        w.main_window.add_text("the penguin slipped off the ice rink. they want food now.")

    if chance() <= 20:
        w.main_window.add_text("the penguin yearns for sashimi. maybe you should go to the fish market?")

    if chance() <= 25:
        w.main_window.add_text("the clouds are deforming. expect the sun to appear.")

    if chance() <= 6:
        w.main_window.add_text("the penguin is going to the groceries without consent. but they need your help to buy stuff. please?")
        st.grocery()

    if chance() <= 3:
        w.main_window.add_text("the penguin is going to the fish market without consent. but they need your help to buy stuff (especially the sashimi). please?")
        fm.fish_market()

    if chance() <= 30:
        w.main_window.add_text("the penguin would like to go fishing now. consider fishing?")

    if chance() <= 4:
        w.main_window.add_text("the penguin will go fishing without your consent. but you still need to fish.")
        fishing.fishing()

    if chance() <= 3:
        w.main_window.add_text(f"{s.p.name} is going to ask itself what to do. don't blame it.")
        wtd.what_do()

    if chance() <= 2:
        w.main_window.add_text(f"{s.p.name} is going to do a random thing. beware.")
        random_thing = r.choice(list(w.main_window.keywords.values()))
        w.main_window.add_text(f"it is going to do {random_thing.__name__}.")
        if random_thing.__name__ == "exit_command":
            w.main_window.add_text("... but it couldn't because it was too dangerous. aww well.")
            w.main_window.after(50, random_event_loop)
            return
        random_thing()

    if chance() <= 3:
        w.main_window.add_text(f"{s.p.name} is going to eat a random food without anyone's consent.")
        try:
            random_food = r.choice(list(s.p.inventory["edibles"].keys()))
        except IndexError:
            w.main_window.add_text("hm. there seems to be no food at all!")
            return

        w.main_window.add_text(f"and that food is {random_food}! say goodbye to it!")
        eat.eat(random_food)



    w.main_window.after(50, random_event_loop)