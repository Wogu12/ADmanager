import customtkinter as ct

class ButtonMenu(ct.CTk):
    def __init__(self):
        super().__init__()

    def add_new_btn(self, menu_frame, text_con, row_num):
        self.button_add_user = ct.CTkButton(
            menu_frame,
            text = text_con,
            #command = lambda btn_val = "Add": self.button_callback(btn_val),
            # width=(self._window_width / 4),
            # height=(self._window_height / 4),
            )
        self.button_add_user.grid(row = row_num, column = 0, padx = 10, pady = (5, 0), sticky = "nesw")

    # def edit_user(self, menu_frame)
    #     self.button_edit_user = ct.CTkButton(
    #         self.menu_frame,
    #         text = "Edit User",
    #         # command=,
    #         # width=(self._window_width / 4),
    #         # height=(self._window_height / 4),
    #         )
    #     self.button_edit_user.grid(row = 1, column = 0, padx = 10, pady = (5, 0), sticky = "nesw")

    #     self.button_disable_user = ct.CTkButton(
    #         self.menu_frame,
    #         text = "Disable User",
    #         # command=,
    #         # width=(self._window_width / 4),
    #         # height=(self._window_height / 4),
    #         )
    #     self.button_disable_user.grid(row = 2, column = 0, padx = 10, pady = (5, 0), sticky = "nesw")


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