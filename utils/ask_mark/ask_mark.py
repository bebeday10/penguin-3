import penglang.modules.pengcustomersupport as pcs
from .. import window as w
from . import data as d

def ask_mark(model="2", word_amount="50", *question):
    """
    Ask Mark a question.

    SKW:
        model: a number. supply at least that amount of words.
        word_amount: how much it should talk
    """
    try:
        model = int(model)
        word_amount = int(word_amount)

    except ValueError:
        w.main_window.add_text("those aren't numbers!!!")
        return

    question = " ".join(question)
    w.main_window.add_text("asking Mark...")
    mark = pcs.PenguinCustomerSupport(d.data, model)
    mark.brain = mark.to_customer_support_brain(True)
    w.main_window.add_text(f"Mark: {" ".join(mark.talk_to_customer_support(word_amount, return_instead=True, prequestion=question))}")

w.main_window.keywords[
    "ask-mark",
    "mark-ask",
    "why-mark"
] = ask_mark