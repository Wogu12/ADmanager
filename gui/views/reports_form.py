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

        self._controller = controller
        self._users = self._controller.get_names()

        self._pad_X_l = 5
        self._pad_x_r = 5

        ctk.CTkLabel(self, text="Raporty", font=("Arial", 24)).grid(row=0, column=0, columnspan=3, pady=10, sticky='ew')

        ctk.CTkLabel(self, text="Wybierz raporty", font=("Arial", 14)).grid(row=1, column=0, columnspan=3, pady=10, sticky='w')

        _always_on = ctk.IntVar(value=1)
        self.chkbox_users_list = ctk.CTkCheckBox(self, text="Lista użytkowników z podstawowymi danymi.", variable=_always_on, state="disabled").grid(row=2, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_acc_expires = ctk.IntVar(value=0)
        self.chkbox_acc_expires = ctk.CTkCheckBox(self, text="Data wygaśnięcia kont.", variable=self._state_acc_expires).grid(row=3, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_pwd_last_set = ctk.IntVar(value=0)
        self.chkbox_pwd_last_set = ctk.CTkCheckBox(self, text="Data ostatniej zmiany hasła.", variable=self._state_pwd_last_set).grid(row=4, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_acc_locked = ctk.IntVar(value=0)
        self.chkbox_acc_locked = ctk.CTkCheckBox(self, text="Pokaż zablokowane konta.", variable=self._state_acc_locked).grid(row=5, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_show_disabled_acc = ctk.IntVar(value=0)
        self.chkbox_show_disabled_acc = ctk.CTkCheckBox(self, text="Uwzględnij wyłączone konta.", variable=self._state_show_disabled_acc).grid(row=6, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_last_login = ctk.IntVar(value=0)
        self.chkbox_last_login = ctk.CTkCheckBox(self, text="Data ostaniego logowania konta.", variable=self._state_last_login).grid(row=7, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)

        self._state_passwd_expires = ctk.IntVar(value=0)
        self.chkbox_passwd_expires = ctk.CTkCheckBox(self, text="Pokaż, czy hasło straciło ważność.", variable=self._state_passwd_expires).grid(row=8, column=0, columnspan=3, sticky="ew", padx=(self._pad_X_l, self._pad_x_r), pady=2)
                                                 
        self.generate_reports = ctk.CTkButton(self, text="Generuj raport", command=self._generate_reports)
        self.generate_reports.grid(row=9, column=0, columnspan=3, sticky='ew', padx=(self._pad_X_l, self._pad_x_r), pady=5)

    def _generate_reports(self):
        _state_acc_expires = self._state_acc_expires.get()
        _state_pwd_last_set = self._state_pwd_last_set.get()
        _state_acc_locked = self._state_acc_locked.get()
        _state_show_disabled_acc = self._state_show_disabled_acc.get()
        _state_last_login = self._state_last_login.get()
        _state_passwd_expires = self._state_passwd_expires.get()
        
        self._controller.generate_report(_state_acc_expires, _state_pwd_last_set, _state_acc_locked, _state_show_disabled_acc, _state_last_login, _state_passwd_expires)
    
