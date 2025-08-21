from gui.views.edit_user_form import EditUserForm
from ad_functions.edit_user_manager import EditUserManager

class EditUserController:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.edit_user_manager = EditUserManager()

    def show_form(self):
        form = EditUserForm(self, self.parent_frame)
        form.grid(row=0, column=0, sticky="nsew")

    def get_names(self):
        return list(self.edit_user_manager.users_dict.values())

    # def get_organizational_units(self):
    #     return self.edit_user_manager.ous_list
  
    # def get_groups(self):
    #     return self.new_user_manager.groups_list

    # def create_user(self, name, surname, job_title, mail, username, password, ou_dn, groups):
    #     return self.new_user_manager.create_user(name, surname, job_title, mail, username, password, ou_dn, groups)




