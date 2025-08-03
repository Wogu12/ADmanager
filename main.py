from gui.window import Window
from utils.adm_logger import AdmLogger


def main():
    logger = AdmLogger()
    gui_logger = logger.get_logger("gui")

    app = Window(gui_logger)
    app.mainloop()


if __name__ == "__main__":
    main()
