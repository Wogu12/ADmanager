from gui.views.base_form import BaseForm
import customtkinter as ctk


class AddUserForm(BaseForm):
    def __init__(self, controller, parent):
        super().__init__(parent)

        self.controller = controller
        self._ous = self.controller.get_organizational_units()

        label = ctk.CTkLabel(self, text="Add New User", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        ctk.CTkLabel(self, text="Imię:").grid(row=1, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Nazwisko:").grid(row=2, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_surname = ctk.CTkEntry(self)
        self.entry_surname.grid(row=2, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Stanowisko:").grid(row=3, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_surname = ctk.CTkEntry(self)
        self.entry_surname.grid(row=3, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Login:").grid(row=4, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_login = ctk.CTkEntry(self)
        self.entry_login.grid(row=4, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Hasło:").grid(row=5, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_passwd = ctk.CTkEntry(self, show='*')
        self.entry_passwd.grid(row=5, column=1, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Powtórz hasło:").grid(row=6, column=0, sticky="w", padx=(20, 0), pady=5)
        self.entry_repeat = ctk.CTkEntry(self, show='*')
        self.entry_repeat.grid(row=6, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Dział:").grid(row=7, column=0, sticky="w", padx=(20, 5), pady=5)
        self.dropdown_ou = ctk.CTkOptionMenu(self, values=self._ous)
        self.dropdown_ou.grid(row=7, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Grupy:").grid(row=8, column=0, sticky="w", padx=(20, 5), pady=5)
        self.dropdown_group = ctk.CTkOptionMenu(self, values=["Użytkownicy", "Administratorzy", "Goście"])
        self.dropdown_group.grid(row=8, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        self.button_create = ctk.CTkButton(self, text="Dodaj użytkownika", command=self._on_create_user)
        self.button_create.grid(row=9, column=0, columnspan=3, pady=10)

    def _on_create_user(self):
        username = self.entry_login.get()
        password = self.entry_passwd.get()
        ou_dn = self.dropdown_ou.get()  # placeholder
        group_dns = []  # placeholder
        if self.controller.create_user(username, password, ou_dn, group_dns) is not None:
            print('Nowy dodany z formularza')
        else: 
            print('')#dodac obsluge wyjatkow 

        