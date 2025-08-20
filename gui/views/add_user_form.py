from gui.views.base_form import BaseForm
import customtkinter as ctk
import string
from CTkMessagebox import CTkMessagebox
from CTkListbox import *


class AddUserForm(BaseForm):
    def __init__(self, controller, parent):
        super().__init__(parent)

        self._controller = controller
        self._ous = self._controller.get_organizational_units()
        self._groups = self._controller.get_groups()

        label = ctk.CTkLabel(self, text="Add New User", font=("Arial", 16))
        label.grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        ctk.CTkLabel(self, text="Imię:").grid(row=1, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.grid(row=1, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Nazwisko:").grid(row=2, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_surname = ctk.CTkEntry(self)
        self.entry_surname.grid(row=2, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Stanowisko:").grid(row=3, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_job_title = ctk.CTkEntry(self)
        self.entry_job_title.grid(row=3, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="E-mail:").grid(row=4, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_mail = ctk.CTkEntry(self)
        self.entry_mail.grid(row=4, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Login:").grid(row=5, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_login = ctk.CTkEntry(self)
        self.entry_login.grid(row=5, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Hasło:").grid(row=6, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_passwd = ctk.CTkEntry(self, show='*')
        self.entry_passwd.grid(row=6, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Powtórz hasło:").grid(row=7, column=0, sticky="w", padx=(20, 0), pady=5)
        self.entry_repeat = ctk.CTkEntry(self, show='*')
        self.entry_repeat.grid(row=7, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Dział:").grid(row=8, column=0, sticky="w", padx=(20, 5), pady=5)
        self.dropdown_ou = ctk.CTkOptionMenu(self, values=self._ous)
        self.dropdown_ou.grid(row=8, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        ctk.CTkLabel(self, text="Grupy:").grid(row=9, column=0, sticky="w", padx=(20, 5), pady=5)
        self.entry_groups = ctk.CTkEntry(self)
        self.entry_groups.grid(row=9, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        self.combobox_groups = ctk.CTkOptionMenu(self, values=self._groups)
        self.combobox_groups.grid(row=11, column=1, sticky="ew", padx=(5, 10), pady=5)

        self.add_group_btn = ctk.CTkButton(self, text="Dodaj", command=self._add_group)
        self.add_group_btn.grid(row=11, column=2, padx=(5, 10), pady=5, sticky="ew")

        self.selected_groups = []

        self.button_create = ctk.CTkButton(self, text="Dodaj użytkownika", command=self._create_user)
        self.button_create.grid(row=12, column=0, columnspan=3, sticky='ew', pady=15, padx=10)

    def _add_group(self):
        group = self.combobox_groups.get()
        if group and group not in self.selected_groups:
            self.selected_groups.append(group)

            self.entry_groups.delete(0, "end")
            self.entry_groups.insert(0, ", ".join(self.selected_groups))

    def _valid_passwd(self):
        _passwd = self.entry_passwd.get()
        _repeat_passwd = self.entry_repeat.get()

        if _passwd != _repeat_passwd:
            return False
        else:
            return True 
    
    def _create_user(self):
        if self._valid_passwd():
            _name = self.entry_name.get()
            _surname = self.entry_surname.get()
            _job_title = self.entry_job_title.get()
            _mail = self.entry_mail.get()
            _username = self.entry_login.get()
            _passwd = self.entry_passwd.get()
            _ou = self.dropdown_ou.get()
            _groups = self.entry_groups.get()
            if self._controller.create_user(_name, _surname, _job_title, _mail, _username, _passwd, _ou, _groups) is not None:
                CTkMessagebox(title="Błąd", message='Nowy użytkownik został pomyślnie dodany')
            else: 
                print('')#dodac obsluge wyjatkow 
        else:
            CTkMessagebox(title="Błąd", message='Login lub haslo nie spelnia wymagan')


        