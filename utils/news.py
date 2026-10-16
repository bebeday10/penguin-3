from . import window as w
from . import state as s
import penglang.modules.pengbulletin.pengbulletinitem as pbi

def news(amount="1"):
    """
    read the latest news from Penguin News.
    SKW:
        amount: the amount of news. default 1.
    """
    news = pbi.PenguinBulletin("")
    try: amount = int(amount)
    except ValueError: w.main_window.add_text("that's not a number!!!"); return None
    for _ in range(amount):
        news.change_random_body()
        w.main_window.add_text(news.get_body())

w.main_window.keywords[
    "news",
    "read-news",
    "penguin-news",
    "latest-news"
] = news