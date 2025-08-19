# import customtkinter as ctk
# # from logic import ButtonLogic
# from utils import AdmLogger
# from .button_menu import ButtonMenu
# from gui.button_menu import ButtonMenu
# from utils.adm_logger import AdmLogger
# from logic.controller import Controller
# import logging
# import sys



# # class Window(ctk.CTk):
#     # _adm_logger = AdmLogger()
#     # def __init__(self):
#     #     # super().__init__()
#     #     # self._logger = self._adm_logger.get_logger("gui")
#     #     # self._logger.info("Initialize main window.")
#     #     # # self._buttons = SideMenu()
#     #     # self._controller = Controller(self)

#     #     # self.geometry("600x500")
#     #     # self.minsize(400, 300)
#     #     # self.title("AD Manager")
        
#     #     # self.draw_window()

#     #     # self._button_logic = ButtonLogic(self._content_frame, self._logger)

#     #     # self._buttons = ButtonMenu(self._menu_frame, self._button_logic)

#     #     # self.protocol("WM_DELETE_WINDOW", self._on_close)
#     #     super().__init__()
#     #     self.logger = AdmLogger().get_logger("gui")
#     #     self.logger.info("Initializing main window...")

#     #     self.controller = Controller(self)

#     #     self.title("AD Manager")
#     #     self.geometry("800x600")
#     #     self.minsize(600, 400)
#     #     self.protocol("WM_DELETE_WINDOW", self._on_close)

#     #     self._create_widgets()
# class Window(ctk.CTk):
#     # def __init__(self):
#     #     super().__init__()
#     #     self.logger = AdmLogger().get_logger("gui")
#     #     self.logger.info("Initializing main window...")

#     #     self.title("AD Manager")
#     #     self.geometry("800x600")
#     #     self.minsize(600, 400)
#     #     self.protocol("WM_DELETE_WINDOW", self._on_close)

#     #     self.controller = None  # <-- tymczasowo
#     #     self._init_controller_later = True  # flaga pomocnicza

#     #     self._create_widgets()  # <- tu NIE potrzebujemy controller

#     #     self.controller = Controller(self)  # <-- dopiero teraz
#     #     self.menu.set_controller(self.controller)   
#     def __init__(self):
#         super().__init__()
#         self.logger = AdmLogger().get_logger("gui")
#         self.logger.info("Initializing main window...")
#         self.title("Active Directory Manager")
#         self.geometry("800x600")

#         self.grid_columnconfigure(1, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         self.menu_frame = ctk.CTkFrame(self)
#         self.menu_frame.grid(row=0, column=0, sticky="ns")

#         self.content_frame = ctk.CTkFrame(self, corner_radius=0)
#         self.content_frame.grid(row=0, column=1, sticky="nsew")

#         self.controller = Controller(self)

#         self._create_widgets()
#         self.protocol('WM_DELETE_WINDOW', self._on_close)

#     def _create_widgets(self):
#         # self.grid_columnconfigure(1, weight=1)
#         # self.grid_rowconfigure(0, weight=1)

#         # self.menu_frame = ctk.CTkFrame(self)
#         # self.menu_frame.grid(row=0, column=0, sticky="nsew")

#         # self.content_frame = ctk.CTkFrame(self)
#         # self.content_frame.grid(row=0, column=1, sticky="nsew")

#         # self.menu = ButtonMenu(self.menu_frame, self.controller)
#         # self.menu.pack(fill="both", expand=True)
#         self.menu = ButtonMenu(self.menu_frame, self.controller)
#         self.menu.grid(row=0, column=0, sticky="nsew")

#     def _on_close(self):
#         self.logger.info("App shutting down.")
#         self.destroy()
#         self.quit()

#     #     self.draw_window()

#     # def draw_window(self):
#     #     self._window_width = self.winfo_width()
#     #     self._window_height = self.winfo_height()

#     #     self.grid_rowconfigure(0, weight=1)
#     #     self.grid_columnconfigure(1, weight=1)

#     #     self._menu_frame = ctk.CTkFrame(self)
#     #     self._menu_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nesw")
#     #     self._menu_frame.grid_columnconfigure((0, 1), weight=1)

#     #     self._content_frame = ctk.CTkFrame(self)
#     #     self._content_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nesw")

#     #     # self._buttons.place_buttons(self._menu_frame)

#     # def _on_close(self):
#     #     self._logger.info("App shutting down.")
#     #     self.destroy()
#     #     self.quit()

import customtkinter as ctk
from gui.button_menu import ButtonMenu
from logic.add_user_controller import AddUserController
from CTkMessagebox import CTkMessagebox


class Window(ctk.CTk):
    def __init__(self, logger):
        super().__init__()
        self.logger = logger
        self.logger.info("Initialize main window.")
        self.title("AD Manager")
        self.geometry("620x500")
        self.minsize(620, 300)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, padx=0, pady=0, sticky="ns")
        self.menu_frame.grid_columnconfigure((0, 1), weight=1)

        # self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        # self.content_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nsew")
        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        try:
            self.controller = AddUserController(self.content_frame)
        except Exception as e:
            self.controller = None
            CTkMessagebox(title="UWAGA", message='Brak połączenia z serwerem Active Directory! Aby móc kontynuować przywróć połączenie z serwerem i zrestartuj aplikację.')

        self._create_widgets()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _create_widgets(self):
        if self.controller is not None:
            self.menu = ButtonMenu(self.menu_frame, self.controller)
            self.menu.grid(row=0, column=0, sticky="nsew")

    def _on_close(self):
        self.logger.info("App shutting down.")
        self.destroy()
        self.quit()
