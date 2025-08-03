# from gui.views.add_user_form import AddUserForm
# # from gui.views.delete_user_form import DeleteUserForm
# # from gui.views.user_details_form import UserDetailsForm
# # from gui.views.group_management_form import GroupManagementForm

# class Controller:
#     def __init__(self, window):
#         self.window = window
#         self.content_frame = self.window.content_frame

#     def _clear_frame(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

#     def show_add_user_form(self):
#         self._clear_frame()
#         AddUserForm(self.content_frame).pack(fill="both", expand=True)

#     # def show_delete_user_form(self):
#     #     self._clear_frame()
#     #     DeleteUserForm(self.content_frame).pack(fill="both", expand=True)

#     # def show_user_details_form(self):
#     #     self._clear_frame()
#     #     UserDetailsForm(self.content_frame).pack(fill="both", expand=True)

#     # def show_group_management_form(self):
#     #     self._clear_frame()
#     #     GroupManagementForm(self.content_frame).pack(fill="both", expand=True)

############################################################################################3

# from gui.views.add_user_form import AddUserForm

# class AddUserController:
#     def __init__(self, window):
#         self.window = window
#         self.content_frame = window.content_frame

#     def show_add_user_form(self):
#         self._clear_content()
        
#         form = AddUserForm(self.content_frame)
#         form.grid(row=0, column=0, sticky="new")

#     def _clear_content(self):
#         for widget in self.content_frame.winfo_children():
#             widget.destroy()

from gui.views.add_user_form import AddUserForm
from ad_functions.test import AdConnectorBaseClass

class AddUserController:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.user_manager = AdConnectorBaseClass()

    def show_form(self):
        form = AddUserForm(self, self.parent_frame)
        form.grid(row=0, column=0, sticky="nsew")

    def get_organizational_units(self):
        return self.user_manager.get_ous()

    # def get_groups(self):
    #     return self.user_manager.get_all_groups()

    def create_user(self, username, password, ou_dn, group_dns):
        return self.user_manager.create_user(username, password, ou_dn, group_dns)




