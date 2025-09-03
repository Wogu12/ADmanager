from gui.views.reports_form import ReportsForm
from ad_functions.reports_manager import ReportsManager

class RaportsController:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.new_user_manager = ReportsManager()

    def show_form(self):
        form = ReportsForm(self, self.parent_frame)
        form.grid(row=0, column=0, sticky="nsew")

    # def get_organizational_units(self):
    #     return list(self.new_user_manager.mapped_ous.keys())
  
    # def get_groups(self):
    #     return self.new_user_manager.groups_list

    # def create_user(self, name, surname, job_title, mail, username, password, ou_dn, groups):
    #     return self.new_user_manager.create_user(name, surname, job_title, mail, username, password, ou_dn, groups)

