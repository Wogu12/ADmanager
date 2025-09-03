import customtkinter as ctk


class ButtonMenu(ctk.CTkFrame):
    def __init__(self, parent, controller, button_txt):
        super().__init__(master=parent, fg_color="transparent")
        self.controller = controller

        if button_txt == 'Dodaj użytkownika':
            self._create_button(button_txt, 0, 0, self._add_user)
        if button_txt == 'Edytuj użytkownika':
            self._create_button(button_txt, 1, 0, self._edit_user)
        if button_txt == 'Raporty':
            self._create_button(button_txt, 2, 0, self._reports)

    def _create_button(self, text, row, column, cmd):
        button = ctk.CTkButton(self, text=text, command=cmd, font=("Arial", 12, "bold"), height=48)
        button.grid(row=row, column=column, padx=10, pady=(5, 0), sticky="ew")

    def _add_user(self):
        self.controller.show_form()

    def _edit_user(self):
        self.controller.show_form()

    def _reports(self):
        self.controller.show_form()