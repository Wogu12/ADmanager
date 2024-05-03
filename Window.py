import customtkinter as ct
from ButtonMenu import ButtonMenu

class Window(ct.CTk):

    _window_width: float    
    _window_height: float

    buttons = ButtonMenu()

    def __init__(self):
        super().__init__()

        

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

        self.buttons.place_buttons(self.menu_frame)



def main():
    app = Window()
    app.mainloop()

if __name__ == "__main__":
    main()
        
