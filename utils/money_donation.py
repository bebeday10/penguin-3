from . import state as s
from . import window as w

def money_donation(amount="1.0"):
    """
    donate some money to charity. money cannot be returned.

    amount (number): amount of cash to donate
    """
    try:
        amount = float(amount)
    except ValueError:
        w.main_window.add_text("that's not a number!!!")
        return

    if amount > s.p.cash:
        w.main_window.add_text(f"{s.p.name} doesn't have that much money!!!")
        return

    s.p.cash -= amount
    s.p.charity_cash += amount

    w.main_window.add_text(f"${amount} of cash gave to charity!! ${s.p.cash} left, charity now has ${s.p.charity_cash}! 🎉💸")

w.main_window.keywords[
    "donate",
    "donate-money",
    "money-donate",
    "money-donation"
] = money_donation