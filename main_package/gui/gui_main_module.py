import os
from os import listdir
import tkinter as tk
from tkinter import ttk, Button, StringVar, END
from main_package.use_module import Use
from main_package.gui.gui_main_side_module import GuiMainSideMenus
from main_package.gui.gui_profile_module import GuiProfileMenus

class NoteManagerGui(tk.Tk):
    ud_json = os.path.join('userdata', 'user.json')

    def __init__(self):
        super().__init__()
        self.temp_user = StringVar()
        self.side_menus = GuiMainSideMenus(self, self)
        self.profile_menus = GuiProfileMenus(self, self.show_main_menu, self.show_main_menu, self.temp_user)
        self.create_main_menu()
        self.show_menu(self.main_menu_frame)

    def show_menu(self, frame):
        frame.tkraise()

    def show_main_menu(self):
        self.show_menu(self.main_menu_frame)

    def show_profile_menu(self, name):
        self.temp_user = name
        self.profile_menus.create_profile_menu(name)
        self.show_menu(self.profile_menus.profile_menu_frame)

    def cbutton(self, text, size, co, ro, cframe, funct):
        button = Button(
            cframe, text=f"{text}",
            bg="#1c1515", fg="#ebd3d6",
            activebackground="#4a3938", activeforeground="#ab6a72",
            borderwidth=0, width=20, height=2,
            command=funct, font=("Arial", int(size), "bold"), relief='flat'
        )
        button.grid(column=co, row=ro, sticky='n')
        return button

    def create_main_menu(self):
        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure('dark_mode.TFrame', background='#2e2223')
        sty.configure('Main_text.TLabel', background='#2e2223', foreground='#ebd3d6', font=("Arial", 24, "bold"))
        sty.configure('Custom.TEntry', foreground='#ebd3d6', fieldbackground='#1c1515', padding=5, font=('Arial', 14))
        sty.configure('BackgroundOnly.TEntry', background="#1c1515", fieldbackground='BackgroundOnly.TEntry')
        self.title('Note Manager by PGFerraz')
        self.geometry('800x600')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.main_menu_frame = ttk.Frame(self, style='dark_mode.TFrame')
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.main_menu_frame.rowconfigure(0, weight=1)
        self.main_menu_frame.rowconfigure(10, weight=1)
        self.main_menu_frame.columnconfigure(0, weight=1)
        self.main_menu_frame.columnconfigure(10, weight=1)

        main_label = ttk.Label(self.main_menu_frame, text="Note Manager GUI", style='Main_text.TLabel')
        main_label.grid(column=5, row=0, pady=20, sticky='n')

        self.cbutton('Add an User ➕', 12, 5, 1, self.main_menu_frame, lambda: self.show_menu(self.side_menus.add_menu_frame))
        self.cbutton('Remove a User ❌', 12, 5, 2, self.main_menu_frame, lambda: self.show_menu(self.side_menus.remo_menu_frame))
        self.cbutton('Log-In', 12, 5, 3, self.main_menu_frame, lambda: self.show_menu(self.side_menus.login_menu_frame))