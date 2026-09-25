from dataclasses import dataclass
from . import paths as p
from . import data as d



@dataclass
class Penguin:
    garbage: int = 0
    cash: float = 0.0
    name: str = "penguin"
    DEFAULT_DATA = {
        "garbage": 0,
        "cash": 0.0,
        "name": "penguin",

    }
    """
    the default data for the penguin
    """

    def save_data(self):
        data = {
            "garbage": self.garbage,
            "cash": self.cash,
            "name": self.name,
        }
        d.save_data(
            data,
            "save.json"
        )

    def load_data(self):
        data = d.load_data(
            p.BASE_DIR.parent / "penguin-3-data" / "save.json",
            self.DEFAULT_DATA
        )
        for key, value in data.items():
            setattr(self, key, value)
        