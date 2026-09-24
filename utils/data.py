import json as j

from .paths import BASE_DIR

def save_data(data, filename):
    filepath = BASE_DIR / filename
    with open(filepath, "w") as f: 
        j.dump(
            data,
            f,
            indent=4,
            sort_keys=True,
            ensure_ascii=False
        )

def load_data(filename, default):
    try:
        with open(filename, "r") as f:
            data = j.load(f)
    except (FileNotFoundError, j.JSONDecodeError):
        data = {}

    return default | data