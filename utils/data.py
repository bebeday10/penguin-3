import json as j

from .paths import BASE_DIR

def save_data(data, filename):
    filepath = BASE_DIR.parent / "penguin-3-data"
    filepath.mkdir(exist_ok=True)
    save = filepath / filename
    with open(save, "w") as f: 
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