from . import window as w
from . import state as s
from . import paths as s

import penglang.modules.pengfancywindow as pfw
def penguin_3_image():
    """see the logo for Penguin 3"""
    image_window = pfw.PenguinFancyWindow(size="600x600", window_title="logo")
    image_window.app_icon(s.IMAGE_DIR / "penguin_icon.png")
    image_window.add_image("penguin 3 image", s.IMAGE_DIR / "penguin_icon.png", image_size=(512, 512))

w.main_window.keywords[
    "logo",
    "penguin-3-logo",
    "logo-image",
    "penguin-3-image",
    "logo-img",
    "penguin-3-img"
] = penguin_3_image