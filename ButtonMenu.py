import customtkinter as ct

class ButtonMenu(ct.CTk):
    def __init__(self):
        super().__init__()

    def place_buttons(self, parent_cont):
        self.button_add_user = ct.CTkButton(
            parent_cont,
            text = "Add New User",
            command = lambda btn_val = "Add": self.button_callback(btn_val),
            )
        self.button_add_user.grid(row = 0, column = 0, padx = 10, pady = (5, 0))

        self.button_edit_user = ct.CTkButton(
            parent_cont,
            text = "Edit User",
            command = lambda btn_val = "Edit": self.button_callback(btn_val),
            )
        self.button_edit_user.grid(row = 1, column = 0, padx = 10, pady = (5, 0))

        self.button_disable_user = ct.CTkButton(
            parent_cont,
            text = "Disable User",
            command = lambda btn_val = "Disable": self.button_callback(btn_val),
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


# def main():
#     app = ct.CTk()


#     def optionmenu_callback(choice):
#         print("optionmenu dropdown clicked:", choice)

#     optionmenu_var = ct.StringVar(value="option 2")
#     optionmenu = ct.CTkOptionMenu(app,values=["option 1", "option 2"],
#                                          command=optionmenu_callback,
#                                          variable=optionmenu_var)

#     app.mainloop()

# if __name__ == "__main__":
#     main()