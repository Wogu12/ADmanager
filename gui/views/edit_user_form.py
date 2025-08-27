from gui.views.base_form import BaseForm
import customtkinter as ctk
import string
from CTkMessagebox import CTkMessagebox
from CTkListbox import *
import tkinter as tk
from datetime import date


class EditUserForm(BaseForm):
    def __init__(self, controller, parent):
        super().__init__(parent)

        self._controller = controller
        self._users = self._controller.get_names()
        self._groups = self._controller.get_groups()
        self._ous = self._controller.get_organizational_units()

        ctk.CTkLabel(self, text="Edit User", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        ctk.CTkLabel(self, text="Użytkownik:").grid(row=1, column=0, sticky="w", padx=(10, 5), pady=5)
        self.dropdown_user = ctk.CTkOptionMenu(self, values=list(self._users.values()))
        self.dropdown_user.grid(row=1, column=1, sticky="ew", padx=(5, 10), pady=5)

        self.add_group_btn = ctk.CTkButton(self, text="Wybierz", command=self._show_user_data)
        self.add_group_btn.grid(row=1, column=2, sticky='ew', padx=10, pady=5)

        ctk.CTkLabel(self, text="Dane podstawowe", font=("Arial", 12)).grid(row=2, column=0, columnspan=3, padx=(10, 5), pady=2, sticky='w')

        ctk.CTkLabel(self, text="Imię:").grid(row=3, column=0, sticky="w", padx=(10, 10), pady=2)
        self._entry_name_value = tk.StringVar(value='')
        self.entry_name = ctk.CTkEntry(self, textvariable=self._entry_name_value)
        self.entry_name.grid(row=3, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Nazwisko:").grid(row=4, column=0, sticky="w", padx=(10, 5), pady=2)
        self._entry_surname_value = tk.StringVar(value='')
        self.entry_surname = ctk.CTkEntry(self, textvariable=self._entry_surname_value)
        self.entry_surname.grid(row=4, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Stanowisko:").grid(row=5, column=0, sticky="w", padx=(10, 5), pady=2)
        self._entry_job_title_value = tk.StringVar(value='')
        self.entry_job_title = ctk.CTkEntry(self, textvariable=self._entry_job_title_value)
        self.entry_job_title.grid(row=5, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="E-mail:").grid(row=6, column=0, sticky="w", padx=(10, 5), pady=2)
        self._entry_mail_value = tk.StringVar(value='')
        self.entry_mail = ctk.CTkEntry(self, textvariable=self._entry_mail_value)
        self.entry_mail.grid(row=6, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Login:").grid(row=7, column=0, sticky="w", padx=(10, 5), pady=2)
        self._entry_login_value = tk.StringVar(value='')
        self.entry_login = ctk.CTkEntry(self, textvariable=self._entry_login_value)
        self.entry_login.grid(row=7, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Dział:").grid(row=8, column=0, sticky="w", padx=(10, 5), pady=2)
        self.dropdown_ou = ctk.CTkOptionMenu(self, values=self._ous)
        self.dropdown_ou.grid(row=8, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Grupy:").grid(row=9, column=0, sticky="w", padx=(10, 5), pady=2)
        # _entry_login_value = tk.StringVar(value=_data.get('login'))
        self.entry_groups = ctk.CTkEntry(self)
        self.entry_groups.grid(row=9, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        # self.add_to_group = ctk.CTkButton(self, text="Dodaj do grupy")
        # self.add_to_group.grid(row=9, column=0, columnspan=3, sticky='ew', padx=10, pady=5)

        ctk.CTkLabel(self, text="Dodaj do grupy:", font=("Arial", 12)).grid(row=10, column=0, columnspan=3, padx=(10, 0), pady=2, sticky='w')
        self.combobox_groups = ctk.CTkOptionMenu(self, values=self._groups)
        self.combobox_groups.grid(row=10, column=1, sticky="ew", padx=(5, 10), pady=5)

        self.add_group_btn = ctk.CTkButton(self, text="Dodaj")#, command=self._add_group)
        self.add_group_btn.grid(row=10, column=2, padx=(5, 10), pady=5, sticky="ew")

        self.edit_user = ctk.CTkButton(self, text="Edytuj podstawowe dane użytkownika")
        self.edit_user.grid(row=11, column=0, columnspan=3, sticky='ew', padx=10, pady=5)

                

    def _show_user_data(self):
        _cn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
        self._controller.get_user_info(_cn)

        _data = self._controller.returned_user_data()
        print(_data)

        self._entry_name_value.set(_data.get('name'))
        self._entry_surname_value.set(_data.get('surname'))
        self._entry_job_title_value.set(_data.get('job_title'))
        self._entry_mail_value.set(_data.get('mail'))
        self._entry_login_value.set(_data.get('login'))

        ctk.CTkLabel(self, text="Zmiana hasła", font=("Arial", 12)).grid(row=12, column=0, columnspan=3, padx=(10, 5), pady=2, sticky='w')

        ctk.CTkLabel(self, text="Nowe hasło:").grid(row=13, column=0, sticky="w", padx=(10, 5), pady=2)
        self.entry_passwd = ctk.CTkEntry(self, show='*')
        self.entry_passwd.grid(row=13, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        ctk.CTkLabel(self, text="Powtórz hasło:").grid(row=14, column=0, sticky="w", padx=(10, 0), pady=2)
        self.entry_repeat = ctk.CTkEntry(self, show='*')
        self.entry_repeat.grid(row=14, column=1, columnspan=3, sticky="ew", padx=(5, 10), pady=2)

        self._force_change = tk.IntVar(value=False)
        self.change_at_logon = ctk.CTkCheckBox(self, text="Użytkownik musi zmienić hasło przy następnym logowaniu", variable=self._force_change).grid(row=15, column=0, columnspan=3, sticky="ew", padx=(10, 0), pady=2)

        self.change_passwd = ctk.CTkButton(self, text="Zmień hasło", command=self._passwd_operations)
        self.change_passwd.grid(row=16, column=0, columnspan=3, sticky='ew', padx=10, pady=5)

        ctk.CTkLabel(self, text="Opcje konta", font=("Arial", 12)).grid(row=17, column=0, columnspan=3, padx=(10, 5), pady=2, sticky='w')

        if _data['ACCOUNTDISABLE']:
            self._is_disabled = tk.IntVar(value=1)
        if not _data['ACCOUNTDISABLE']:
            self._is_disabled = tk.IntVar(value=0)
        self.disable_acc = ctk.CTkCheckBox(self, text="konto użytkownika jest wyłączone", variable=self._is_disabled).grid(row=18, column=0, columnspan=3, sticky="ew", padx=(10, 0), pady=2)

        self._locked = tk.IntVar(value=0)
        self.unlock_acc = ctk.CTkCheckBox(self, text="Odblokuj konto użytkownika", variable=self._locked).grid(row=19, column=0, columnspan=3, sticky="ew", padx=(10, 0), pady=2)

        self.change_options = ctk.CTkButton(self, text="Edytuj opcje konta", command=self._edit_options)
        self.change_options.grid(row=20, column=0, columnspan=3, sticky='ew', padx=10, pady=5)

    def _passwd_operations(self):
        _dn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
        _passwd = self.entry_passwd.get()
        _repeat_passwd = self.entry_repeat.get()
        _change_at_logon = self._force_change.get()

        if _passwd == _repeat_passwd and len(_passwd) > 0:
            self._controller.change_passwd(_dn, _passwd, _change_at_logon)
            self.entry_passwd.delete(0, "end")
            self.entry_repeat.delete(0, "end")
        else:
            CTkMessagebox(title="Uwaga", message='Hasła nie są takie same.')
        
    def _edit_options(self):
        _dn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
        _disabled = self._is_disabled.get()
        if _disabled == 0:
            self._controller.enable_disable_acc(_dn, 'enable')
        if _disabled == 1:
            self._controller.enable_disable_acc(_dn, 'disable')

        _locked = self._locked.get()
        if _locked == 1:
            self._controller.unlock_acc(_dn)
            self._locked.set(0)

    # def _add_group(self):
    #     group = self.combobox_groups.get()
    #     if group and group not in self.selected_groups:
    #         self.selected_groups.append(group)

    #         self.entry_groups.delete(0, "end")
    #         self.entry_groups.insert(0, ", ".join(self.selected_groups))

    # def _valid_passwd(self):
    #     _passwd = self.entry_passwd.get()
    #     _repeat_passwd = self.entry_repeat.get()

    #     if _passwd != _repeat_passwd:
    #         return False
    #     else:
    #         return True 
    
    # def _create_user(self):
    #     if self._valid_passwd():
    #         _name = self.entry_name.get()
    #         _surname = self.entry_surname.get()
    #         _job_title = self.entry_job_title.get()
    #         _mail = self.entry_mail.get()
    #         _username = self.entry_login.get()
    #         _passwd = self.entry_passwd.get()
    #         _ou = self.dropdown_ou.get()
    #         _groups = self.entry_groups.get()
    #         if self._controller.create_user(_name, _surname, _job_title, _mail, _username, _passwd, _ou, _groups) is not None:
    #             CTkMessagebox(title="Sukces", message='Nowy użytkownik został pomyślnie dodany')
    #     else:
    #         CTkMessagebox(title="Błąd", message='Login lub haslo nie spelnia wymagan')


        
        