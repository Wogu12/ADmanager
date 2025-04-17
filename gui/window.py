import customtkinter as ct
from logic.button_menu import ButtonMenu
from utils import AdmLogger
import logging
import sys



class Window(ct.CTk):
    _adm_logger = AdmLogger()
    def __init__(self):
        super().__init__()
        self._logger = self._adm_logger.get_logger("gui")
        self._logger.info("Initialize main window.")
        self._buttons = ButtonMenu()
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.draw_window()

    def draw_window(self):
        self.geometry("600x500")
        self.minsize(400, 300)
        self.title("AD Manager")

        self._window_width = self.winfo_width()
        self._window_height = self.winfo_height()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self._menu_frame = ct.CTkFrame(self)
        self._menu_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nesw")
        self._menu_frame.grid_columnconfigure((0, 1), weight=1)

        self._content_frame = ct.CTkFrame(self)
        self._content_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nesw")

        self._buttons.place_buttons(self._menu_frame)

    def _on_close(self):
        self._logger.info("App shutting down.")
        self.destroy()
        self.quit()

