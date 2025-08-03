from logic.add_user_controller import AddUserController

class MainController:
    def __init__(self, window):
        self.window = window
        self.content_frame = window.content_frame

        self.add_user_controller = AddUserController(self.content_frame)

    def show_add_user_form(self):
        self._clear_content()
        self.add_user_controller.show_form()

    def _clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()