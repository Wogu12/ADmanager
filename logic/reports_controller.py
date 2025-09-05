from gui.views.reports_form import ReportsForm
from ad_functions.reports_manager import ReportsManager

class RaportsController:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.reports_manager = ReportsManager()

    def show_form(self):
        form = ReportsForm(self, self.parent_frame)
        form.grid(row=0, column=0, sticky="nsew")

    def get_names(self):
        return self.reports_manager.users_dict
    
    def generate_report(self):
        return self.reports_manager.generate_report()

