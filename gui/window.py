import customtkinter as ctk
from gui.button_menu import ButtonMenu
from logic.add_user_controller import AddUserController
from logic.edit_user_controller import EditUserController
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

        self.content_frame = ctk.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, padx=(10, 0), pady=0, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        try:
            self.add_user_controller = AddUserController(self.content_frame)
            self.edit_user_controller = EditUserController(self.content_frame)
        except Exception as e:
            self.add_user_controller = None
            CTkMessagebox(title="UWAGA", message='Brak połączenia z serwerem Active Directory! Aby móc kontynuować przywróć połączenie z serwerem i zrestartuj aplikację.')

        self._create_widgets()
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _create_widgets(self):
        if self.add_user_controller is not None:
            self.button_add_new = ButtonMenu(self.menu_frame, self.add_user_controller, 'Add User')
            self.button_add_new.grid(row=0, column=0, sticky="nsew")
            
            self.button_edit = ButtonMenu(self.menu_frame, self.edit_user_controller, 'Edit User')
            self.button_edit.grid(row=1, column=0, sticky="nsew")

    def _on_close(self):
        self.logger.info("App shutting down.")
        self.destroy()
        self.quit()
