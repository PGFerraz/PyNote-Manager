from tkinter import *
from tkinter import ttk

class GuiProfileMenus:
    def __init__(self, root, show_menu, return_callback):
        self.root = root
        self.show_menu = show_menu
        self.return_callback = return_callback

    def create_profile_menu(self, name):
        self.profile_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.profile_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.profile_menu_frame.rowconfigure(0, weight=1)
        self.profile_menu_frame.rowconfigure(10, weight=1)
        self.profile_menu_frame.columnconfigure(0, weight=1)
        self.profile_menu_frame.columnconfigure(10, weight=1)

        profile_label = ttk.Label(self.profile_menu_frame, text=f"{name} Profile Menu", style='Main_text.TLabel')
        profile_label.grid(column=5, row=0, pady=20, sticky='ns')

        view_notes_button = Button(
            self.profile_menu_frame, text='View Notes',
            command=lambda: self.show_menu(self.return_callback),
            bg="#1c1515", fg="#ebd3d6", width=20, height=2
        )
        view_notes_button.grid(column=5, row=1)

        return_button = Button(
            self.profile_menu_frame, text='Return',
            command=lambda: self.show_menu(self.return_callback),
            bg="#1c1515", fg="#ebd3d6", width=20, height=2
        )
        return_button.grid(column=5, row=2)
