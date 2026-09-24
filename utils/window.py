import penglang.modules.pengfancywindow as pfw
from . import paths as p
from . import state as s
manager = pfw.PenguinFancyWindowManager()

main_window = pfw.PenguinIceWindow(
    manager=manager,
    keyword_not_found_message="the penguin doesn't know what that means... :(",
    before_exit=s.p.save_data
)

main_window.app_icon(p.IMAGE_DIR / "penguin_icon.png")
main_window.add_image("penguin 3", p.IMAGE_DIR / "penguin_icon.png", owner=main_window.widgets["Main Frame"], image_size=(128, 128))