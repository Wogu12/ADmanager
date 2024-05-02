import customtkinter as ct
#from ButtonMenu import ButtonMenu

class Window(ct.CTk):

    _window_width: float    
    _window_height: float

    def __init__(self):
        super().__init__()

        #self.button_menu = ButtonMenu()

        self.geometry("600x500")

        self.minsize(400, 300)

        self.title("AD Manager")

        self._window_width = self.winfo_width()
        self._window_height = self.winfo_height()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.menu_frame = ct.CTkFrame(self)
        self.menu_frame.grid(row = 0, column = 0, padx = 0, pady = 0, sticky = "nesw")

        self.menu_frame.grid_columnconfigure((0,1), weight=1)

        self.content_frame = ct.CTkFrame(self)
        self.content_frame.grid(row = 0, column = 1, padx = (10, 0), pady = 0, sticky = "nesw")

        # self.button_menu.add_new_btn(self.menu_frame, "Add New User", 0)

        # self.button_menu.add_new_btn(self.menu_frame, "Edit User", 1)

        # self.button_menu.add_new_btn(self.menu_frame, "Disable User", 2)

        self.button_add_user = ct.CTkButton(
            self.menu_frame,
            text = "Add New User",
            command = lambda btn_val = "Add": self.button_callback(btn_val),
            # width=(self._window_width / 4),
            # height=(self._window_height / 4),
            )
        self.button_add_user.grid(row = 0, column = 0, padx = 10, pady = (5, 0))

        self.button_edit_user = ct.CTkButton(
            self.menu_frame,
            text = "Edit User",
            command = lambda btn_val = "Edit": self.button_callback(btn_val),
            # width=(self._window_width / 4),
            # height=(self._window_height / 4),
            )
        self.button_edit_user.grid(row = 1, column = 0, padx = 10, pady = (5, 0))

        self.button_disable_user = ct.CTkButton(
            self.menu_frame,
            text = "Disable User",
            command = lambda btn_val = "Disable": self.button_callback(btn_val),
            # width=(self._window_width / 4),
            # height=(self._window_height / 4),
            )
        self.button_disable_user.grid(row = 2, column = 0, padx = 10, pady = (5, 0))





    def button_callback(self, btn_val):
        match btn_val:
            case "Add":
                print("Add")
            case "Edit":
                print("Edit")
            case "Disable":
                print("Disable")



def main():
    app = Window()
    app.mainloop()

if __name__ == "__main__":
    main()
        
