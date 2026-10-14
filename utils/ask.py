from . import window as w
import random as r
from . import state as s

def ask(question=None, *following):
    """
    ask penguin something

    SKW:
        question: do ask please
    """
    if question is None:
        w.main_window.add_text("ya got asked didncha")
        return

    full_question: str = " ".join([question, *following])
    full_question = full_question.replace("you", "i")
    full_question = full_question.replace(s.p.name.lower(), "i")
    full_question = full_question.replace("me", "you")
    full_question = full_question.replace("my", "your")
    full_question = full_question.replace("?", "")

    random_selection = [
        f"{s.p.name} thinks {full_question} is clearly correct after all because they think it would be \"cool\" to do so.",
        f"{s.p.name} disagrees on whatever you were talking about and REFUSES to listen.",
        f"{s.p.name} asks back you {full_question} because they didn't know what you actually meant, at all.",
        f"{s.p.name} didn't quite catch that. wha-what did you say?",
        f"{s.p.name} thinks {full_question} is because their friends ate a hamburger",
        f"{s.p.name} thinks {full_question} is false",
        f"{s.p.name} says that ain't cool.",
        f"{s.p.name} is currently having a 'memory overload'. please refrain from asking them any questions during this time.",
        f"{s.p.name} thinks {full_question} is true",
        f"in {s.p.name}'s opinion, {full_question} would be nice to have",
        f"in {s.p.name}'s opinion, {full_question} shouldn't be seen at all. but really what they want is to go home.",
        f"{s.p.name} has just told you they REFUSE to listen. we WILL report you to the {s.p.name.upper()} POLICE."
    ]

    w.main_window.add_text(r.choice(random_selection))

w.main_window.keywords[
    "ask",
    "ask-question",
    "ask-important-question",
    "ask-about"
] = ask