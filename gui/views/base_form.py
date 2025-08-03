# import customtkinter as ctk

# class BaseForm(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.pack(padx=20, pady=20, fill="both", expand=True)
import customtkinter as ctk


class BaseForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color='transparent')
        self.grid_columnconfigure(0, weight=0)  # label column
        self.grid_columnconfigure(1, weight=1)

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()


