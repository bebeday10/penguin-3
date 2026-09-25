import penglang.modules.pengfancywindow as pfw
from . import paths as p
from . import state as s
manager = pfw.PenguinFancyWindowManager()

main_window = pfw.PenguinIceWindow(
    manager=manager,
    keyword_not_found_message="the penguin doesn't know what that means... :(",
    before_exit=s.p.save_data,
    window_title="Penguin 3"
)

main_window.app_icon(p.IMAGE_DIR / "penguin_icon.png")
main_window.add_image("penguin 3", p.IMAGE_DIR / "penguin_icon.png", owner=main_window.widgets["Main Frame"], image_size=(128, 128))
main_window.add_text("welcome to penguin 3!")
main_window.add_text("you can type keywords in the entry box, such as 'help' or 'keyword-list'. try it out!")