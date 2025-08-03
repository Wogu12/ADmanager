# # import customtkinter as ctk

# # class ButtonMenu(ctk.CTkFrame):
# #     def __init__(self, parent, controller=None):
# #         super().__init__(parent)
# #         self.controller = controller
# #         self._create_button()

# #     def set_controller(self, controller):
# #         self.controller = controller

# #     # def place_buttons(self, parent):
# #     #     # self.button_add_user = ctk.CTkButton(
# #     #     #     parent,
# #     #     #     text = "Add New User",
# #     #     #     command = lambda btn_val = "Add": self._button_callback(btn_val),
# #     #     #     )
# #     #     # self.button_add_user.grid(row = 0, column = 0, padx = 10, pady = (5, 0))

# #     #     # self.button_edit_user = ctk.CTkButton(
# #     #     #     parent,
# #     #     #     text = "Edit User",
# #     #     #     command = lambda btn_val = "Edit": self._button_callback(btn_val),
# #     #     #     )
# #     #     # self.button_edit_user.grid(row = 1, column = 0, padx = 10, pady = (5, 0))

# #     #     # self.button_disable_user = ctk.CTkButton(
# #     #     #     parent,
# #     #     #     text = "Disable User",
# #     #     #     command = lambda btn_val = "Disable": self._button_callback(btn_val),
# #     #     #     )
# #     #     # self.button_disable_user.grid(row = 2, column = 0, padx = 10, pady = (5, 0))

# #     #     # self.button_test = ctk.CTkButton(
# #     #     #     parent,
# #     #     #     text = "test",
# #     #     #     command = self.test,
# #     #     #     )
# #     #     # self.button_test.grid(row = 3, column = 0, padx = 10, pady = (5, 0))
# #     #     self.button_add_user = self._create_button(
# #     #         parent, "Add New User", 0, 0,
# #     #         lambda: self._button_callback("Add")
# #     #     )
# #     #     self.button_edit_user = self._create_button(
# #     #         parent, "Edit User", 1, 0,
# #     #         lambda: self._button_callback("Edit")
# #     #     )
# #     #     self.button_disable_user = self._create_button(
# #     #         parent, "Disable User", 2, 0,
# #     #         lambda: self._button_callback("Disable")
# #     #     )
# #     # def place_buttons(self, parent):
# #     #     # buttons = [
# #     #     #     ("Add New User", "Add"),
# #     #     #     ("Edit User", "Edit"),
# #     #     #     ("Disable User", "Disable"),
# #     #     # ]

# #     #     # for i, (label, key) in enumerate(buttons):
# #     #     #     setattr(self, f"button_{key.lower()}",
# #     #     #             self._create_button(parent, 
# #     #     #                                 label, 
# #     #     #                                 i, 
# #     #     #                                 0,
# #     #     #                                 lambda k=key: self._button_callback(k)
# #     #     #                                 )
# #     #     #             )
# #     #     self.button_add_user = self._create_button(
# #     #         parent, "Add User", 0, 0, self._actions_handler.add_user
# #     #     )
# #     #     # self.button_edit_user = self._create_button(
# #     #     #     parent, "Edit User", 1, 0, self._actions_handler.edit_user
# #     #     # )

# #     def _create_button(self, parent, text, row, column, cmd):
# #         buttons = [
# #             ("Add User", self.controller.show_add_user_form),
# #             ("Delete User", self.controller.show_delete_user_form),
# #             ("User Details", self.controller.show_user_details_form),
# #             ("Group Management", self.controller.show_group_management_form),
# #         ]

# #         for i, (text, command) in enumerate(buttons):
# #             btn = ctk.CTkButton(self, text=text, command=command)
# #             btn.grid(row=i, column=0, padx=10, pady=5, sticky="ew")
# import customtkinter as ctk

# class ButtonMenu(ctk.CTkFrame):
#     def __init__(self, parent, controller=None):
#         super().__init__(parent)
#         self.controller = controller
#         self.grid(row=0, column=0, sticky="ns")

#         self._create_buttons()

#     def _create_button(self, parent, text, row, column, cmd):
#         button = ctk.CTkButton(parent, text=text, command=cmd)
#         button.grid(row=row, column=column, padx=10, pady=(5, 0), sticky="ew")

#     def _create_buttons(self):
#         self._create_button(self, "Add User", row=0, column=0, cmd=self._add_user)
#         self._create_button(self, "Delete User", row=1, column=0, cmd=self._delete_user)

#     def _add_user(self):
#         if self.controller:
#             self.controller.show_add_user_form()

#     def _delete_user(self):
#         if self.controller:
#             self.controller.show_delete_user_form()

#     def set_controller(self, controller):
#         self.controller = controller
import customtkinter as ctk


class ButtonMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent)
        self.controller = controller

        self._create_button("Add User", 0, 0, self._add_user)
        # Możesz dodać kolejne przyciski tutaj

    def _create_button(self, text, row, column, cmd):
        button = ctk.CTkButton(self, text=text, command=cmd)
        button.grid(row=row, column=column, padx=10, pady=(5, 0), sticky="ew")

    def _add_user(self):
        self.controller.show_form()