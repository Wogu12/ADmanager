import customtkinter as ctk


class ButtonMenu(ctk.CTkFrame):
    def __init__(self, parent, controller, button_txt):
        super().__init__(master=parent)
        self.controller = controller

        if button_txt == 'Add User':
            self._create_button(button_txt, 0, 0, self._add_user)
        if button_txt == 'Edit User':
            self._create_button(button_txt, 1, 0, self._edit_user)
        # Możesz dodać kolejne przyciski tutaj

    def _create_button(self, text, row, column, cmd):
        button = ctk.CTkButton(self, text=text, command=cmd)
        button.grid(row=row, column=column, padx=10, pady=(5, 0), sticky="ew")

    def _add_user(self):
        self.controller.show_form()

    def _edit_user(self):
        self.controller.show_form()