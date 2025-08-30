from gui.views.edit_user_form import EditUserForm
from ad_functions.edit_user_manager import EditUserManager

class EditUserController:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.edit_user_manager = EditUserManager()

    def show_form(self):
        form = EditUserForm(self, self.parent_frame)
        form.grid(row=0, column=0, sticky="nsew")

    def get_organizational_units(self):
        return list(self.edit_user_manager.mapped_ous.keys())

    def get_names(self):
        return self.edit_user_manager.users_dict
    
    def get_user_info(self, cn):
        return self.edit_user_manager.get_user_info(cn)
    
    def get_groups(self):
        return self.edit_user_manager.groups_list
    
    def returned_user_data(self):
        return self.edit_user_manager.user_data

    def unlock_acc(self, dn):
        return self.edit_user_manager.unlock_acc(dn)
    
    def enable_disable_acc(self, dn, option):
        return self.edit_user_manager.enable_disable_acc(dn, option)
    
    def change_passwd(self, dn, password, change_at_logon):
        return self.edit_user_manager.change_passwd(dn, password, change_at_logon)
    
    def edit_user_data(self, dn, new_name, new_surname, new_job_title, new_mail, new_ou, to_remove, to_add):
        return self.edit_user_manager.edit_user_data(dn, new_name, new_surname, new_job_title, new_mail, new_ou, to_remove, to_add)
    # def get_organizational_units(self):
    #     return self.edit_user_manager.ous_list
  
    # def get_groups(self):
    #     return self.new_user_manager.groups_list

    # def create_user(self, name, surname, job_title, mail, username, password, ou_dn, groups):
    #     return self.new_user_manager.create_user(name, surname, job_title, mail, username, password, ou_dn, groups)




