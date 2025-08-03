from gui.views.base_form import BaseForm
import customtkinter as ctk
import string


class AddUserForm(BaseForm):
    def __init__(self, controller, parent):
        super().__init__(parent)

        self._controller = controller
        self._ous = self._controller.get_organizational_units()

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
        self.dropdown_group = ctk.CTkOptionMenu(self, values=["test1", "Administratorzy", "Goście"])
        self.dropdown_group.grid(row=8, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=5)

        self.button_create = ctk.CTkButton(self, text="Dodaj użytkownika", command=self._create_user)
        self.button_create.grid(row=9, column=0, columnspan=3, sticky='ew', pady=15)

    def _valid_passwd(self):
        _passwd = self.entry_passwd.get()
        _repeat_passwd = self.entry_repeat.get()

        if len(_passwd) < 8: #do zmiany na 12??????
            return False
        if _passwd != _repeat_passwd:
            return False
        
        lower = any(sign.islower() for sign in _passwd)
        upper = any(sign.isupper() for sign in _passwd)
        number = any(sign.isdigit() for sign in _passwd)
        spec_char = any(sign in string.punctuation for sign in _passwd)
        
        return all([lower, upper, number, spec_char])
    
    def _create_user(self):
        if self._valid_passwd() and len(self.entry_login.get()) >= 4:
            _username = self.entry_login.get()
            _passwd = self.entry_passwd.get()
            _ou = self.dropdown_ou.get()
            group_dns = []  # placeholder
            if self._controller.create_user(_username, _passwd, _ou, group_dns) is not None:
                print('Nowy dodany z formularza')
            else: 
                print('')#dodac obsluge wyjatkow 
        else:
            print('login lub haslo nie spelnia wymagan')

        