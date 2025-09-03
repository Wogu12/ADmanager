from gui.views.base_form import BaseForm
import customtkinter as ctk
import string
from CTkMessagebox import CTkMessagebox
from CTkListbox import *
import tkinter as tk
from datetime import date
import re


class ReportsForm(BaseForm):
    def __init__(self, controller, parent):
        super().__init__(parent)

        # self._controller = controller
        # self._users = self._controller.get_names()
        # self._groups = self._controller.get_groups()
        # self._ous = self._controller.get_organizational_units()
        # self._data = {}

        self._pad_X_l = 5
        self._pad_x_r = 5

        # self._entry_name_value = tk.StringVar(value='')
        # self._entry_surname_value = tk.StringVar(value='')
        # self._entry_job_title_value = tk.StringVar(value='')
        # self._entry_mail_value = tk.StringVar(value='')
        # self._entry_login_value = tk.StringVar(value='')

        ctk.CTkLabel(self, text="raporty", font=("Arial", 24)).grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        ctk.CTkLabel(self, text="Użytkownik:").grid(row=1, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=5)
        self.dropdown_user = ctk.CTkOptionMenu(self, values=[])
        self.dropdown_user.grid(row=1, column=1, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=5)

    #     self.add_group_btn = ctk.CTkButton(self, text="Wybierz", command=self._show_user_data)
    #     self.add_group_btn.grid(row=1, column=2, sticky='ew', padx=(self._pad_X_l, self._pad_x_r), pady=5)

    # def _show_user_data(self):
    #     _cn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
    #     self._controller.get_user_info(_cn)

    #     self._data = self._controller.returned_user_data()
    #     print(self._data)

    #     self._entry_name_value.set(self._data.get('name'))
    #     self._entry_surname_value.set(self._data.get('surname'))
    #     self._entry_job_title_value.set(self._data.get('job_title'))
    #     self._entry_mail_value.set(self._data.get('mail'))
    #     self._entry_login_value.set(self._data.get('login'))

    #     ctk.CTkLabel(self, text="Dane podstawowe", font=("Arial", 14)).grid(row=2, column=0, columnspan=3, padx=(self._pad_X_l, self._pad_x_r), pady=2, sticky='w')

    #     ctk.CTkLabel(self, text="Imię:").grid(row=3, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_name = ctk.CTkEntry(self, textvariable=self._entry_name_value)
    #     self.entry_name.grid(row=3, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="Nazwisko:").grid(row=4, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_surname = ctk.CTkEntry(self, textvariable=self._entry_surname_value)
    #     self.entry_surname.grid(row=4, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="Stanowisko:").grid(row=5, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_job_title = ctk.CTkEntry(self, textvariable=self._entry_job_title_value)
    #     self.entry_job_title.grid(row=5, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="E-mail:").grid(row=6, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_mail = ctk.CTkEntry(self, textvariable=self._entry_mail_value)
    #     self.entry_mail.grid(row=6, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="Login:").grid(row=7, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_login = ctk.CTkEntry(self, textvariable=self._entry_login_value)
    #     self.entry_login.grid(row=7, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="Dział:").grid(row=8, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.dropdown_ou = ctk.CTkOptionMenu(self, values=self._ous,)
    #     user_dn = self._data.get("user_ou")
        
    #     user_ou = re.sub(r"^CN=[^,]+,", "", user_dn)
    #     ou_key = next((k for k, v in self._controller.edit_user_manager.mapped_ous.items() if v == user_ou), None)

    #     if ou_key:
    #         self.dropdown_ou.set(ou_key)
    #     self.dropdown_ou.grid(row=8, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self.current_groups = list(self._data['groups'].values())

    #     ctk.CTkLabel(self, text="Grupy:").grid(row=9, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.group_entry = ctk.CTkEntry(self, placeholder_text="Grupy")
    #     self.group_entry.insert(0, ", ".join(self.current_groups))
    #     self.group_entry.grid(row=9, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self.edit_groups_btn = ctk.CTkButton(self, text="Edytuj grupy", command=self.open_group_popup)
    #     self.edit_groups_btn.grid(row=10, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self.edit_user = ctk.CTkButton(self, text="Edytuj podstawowe dane użytkownika", command=self.edit_user_data)
    #     self.edit_user.grid(row=11, column=0, columnspan=3, sticky='ew', padx=(self._pad_X_l, self._pad_x_r), pady=5)

    #     ctk.CTkLabel(self, text="Zmiana hasła", font=("Arial", 14)).grid(row=12, column=0, columnspan=3, padx=(self._pad_X_l, self._pad_x_r), pady=2, sticky='w')

    #     ctk.CTkLabel(self, text="Nowe hasło:").grid(row=13, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_passwd = ctk.CTkEntry(self, show='*')
    #     self.entry_passwd.grid(row=13, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     ctk.CTkLabel(self, text="Powtórz hasło:").grid(row=14, column=0, sticky="w", padx=(self._pad_X_l, self._pad_x_r), pady=2)
    #     self.entry_repeat = ctk.CTkEntry(self, show='*')
    #     self.entry_repeat.grid(row=14, column=1, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self._force_change = tk.IntVar(value=False)
    #     self.change_at_logon = ctk.CTkCheckBox(self, text="Użytkownik musi zmienić hasło przy następnym logowaniu", variable=self._force_change).grid(row=15, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self.change_passwd = ctk.CTkButton(self, text="Zmień hasło", command=self._passwd_operations)
    #     self.change_passwd.grid(row=16, column=0, columnspan=3, sticky='ew', padx=(self._pad_X_l, self._pad_x_r), pady=5)

    #     ctk.CTkLabel(self, text="Opcje konta", font=("Arial", 14)).grid(row=17, column=0, columnspan=3, padx=(self._pad_X_l, self._pad_x_r), pady=2, sticky='w')

    #     if self._data['ACCOUNTDISABLE']:
    #         self._is_disabled = tk.IntVar(value=1)
    #     if not self._data['ACCOUNTDISABLE']:
    #         self._is_disabled = tk.IntVar(value=0)
    #     self.disable_acc = ctk.CTkCheckBox(self, text="konto użytkownika jest wyłączone", variable=self._is_disabled).grid(row=18, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self._locked = tk.IntVar(value=0)
    #     self.unlock_acc = ctk.CTkCheckBox(self, text="Odblokuj konto użytkownika", variable=self._locked).grid(row=19, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

    #     self.change_options = ctk.CTkButton(self, text="Edytuj opcje konta", command=self._edit_options)
    #     self.change_options.grid(row=20, column=0, columnspan=3, sticky='ew', padx=(self._pad_X_l, self._pad_x_r), pady=5)

    # def open_group_popup(self):
    #     self.popup = ctk.CTkToplevel(self)
    #     self.popup.title("Edycja grup")
    #     popup_width = 300
    #     popup_height = 300
    #     self.popup.geometry(f"{popup_width}x{popup_height}")
    #     self.popup.attributes("-topmost", True)
    #     self.popup.grab_set()
    #     self.popup.grid_columnconfigure(0, weight=1)

    #     self.popup.update_idletasks()
    #     main_x = self.winfo_rootx()
    #     main_y = self.winfo_rooty()
    #     main_width = self.winfo_width()
    #     main_height = self.winfo_height()

    #     x = main_x + (main_width // 2) - (popup_width // 2)
    #     y = main_y + (main_height // 2) - (popup_height // 2)
    #     self.popup.geometry(f"+{x}+{y}")

    #     self.group_vars = {}

    #     for i, g in enumerate(self._groups):
    #         var = ctk.IntVar(value=1 if g in self.current_groups else 0)
    #         chk = ctk.CTkCheckBox(self.popup, text=g, variable=var)
    #         chk.grid(row=i, column=0, padx=10, pady=2, sticky="w")
    #         self.group_vars[g] = var

    #     save_btn = ctk.CTkButton(self.popup, text="Zapisz", command=self.save_groups_to_entry)
    #     save_btn.grid(row=len(self._groups), column=0, pady=10, padx=10, sticky="ew")

    # def save_groups_to_entry(self):
    #     _selected_groups = [group for group, var in self.group_vars.items() if var.get() == 1]

    #     self.group_entry.delete(0, "end")
    #     self.group_entry.insert(0, ", ".join(_selected_groups))

    #     self.popup.destroy()

    # def edit_user_data(self):
    #     _dn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
    #     _new_name = self.entry_name.get() if self.entry_name.get() != self._data['name'] else None
    #     _new_surname = self.entry_surname.get() if self.entry_surname.get() != self._data['surname'] else None
    #     _new_job_title = self.entry_job_title.get() if self.entry_job_title.get() != self._data['job_title'] else None
    #     _new_mail = self.entry_mail.get() if self.entry_mail.get() != self._data['mail'] else None
    #     _new_ou = self.dropdown_ou.get()
    #     _raw_groups = self.group_entry.get()
    #     _user_groups = [group.strip() for group in _raw_groups.split(",") if group.strip()]

    #     _to_remove = list(set(self.current_groups) - set(_user_groups))
    #     _to_add = list(set(_user_groups) - set(self.current_groups))

    #     self._controller.edit_user_data(_dn, _new_name, _new_surname, _new_job_title, _new_mail, _new_ou, _to_remove, _to_add)
        
    # def _passwd_operations(self):
    #     _dn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
    #     _passwd = self.entry_passwd.get()
    #     _repeat_passwd = self.entry_repeat.get()
    #     _change_at_logon = self._force_change.get()

    #     if _passwd == _repeat_passwd and len(_passwd) > 0:
    #         self._controller.change_passwd(_dn, _passwd, _change_at_logon)
    #         self.entry_passwd.delete(0, "end")
    #         self.entry_repeat.delete(0, "end")
    #     else:
    #         CTkMessagebox(title="Uwaga", message='Hasła nie są takie same.')
        
    # def _edit_options(self):
    #     _dn = [k for k, v in self._users.items() if v == self.dropdown_user.get()]
    #     _disabled = self._is_disabled.get()
    #     if _disabled == 0:
    #         self._controller.enable_disable_acc(_dn, 'enable')
    #     if _disabled == 1:
    #         self._controller.enable_disable_acc(_dn, 'disable')

    #     _locked = self._locked.get()
    #     if _locked == 1:
    #         self._controller.unlock_acc(_dn)
    #         self._locked.set(0)
       
        