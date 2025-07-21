import os
from os import listdir
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk, Button, StringVar, END
from PIL import Image, ImageTk
from main_package.use_module import Use
from main_package.gui.gui_utils import cbutton
from main_package.gui.gui_utils import _custom_main_menu_logo_path as image_path
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

    def create_main_menu(self):
        
        self.title('Note Manager by PGFerraz')
        self.geometry('800x600')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure('dark_mode.TFrame', background='#121212')
        sty.configure('Main_text.TLabel', background='#121212', foreground='#ffffff', font=("Segoe UI", 24, "bold"))
        sty.configure('Sub_text.TLabel', background='#121212', foreground='#ffffff', font=("Segoe UI", 18, "bold"))
        sty.configure('Custom.TEntry', foreground='#ebd3d6', fieldbackground='#1c1515', padding=5, font=("Segoe UI", 14))
        sty.configure('BackgroundOnly.TEntry', background="#1c1515", fieldbackground='BackgroundOnly.TEntry')


        self.main_menu_frame = ttk.Frame(self, style='dark_mode.TFrame')
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.main_menu_frame.rowconfigure(0, weight=1)
        self.main_menu_frame.rowconfigure(4, weight=1)
        self.main_menu_frame.columnconfigure(0, weight=1)
        self.main_menu_frame.columnconfigure(4, weight=1)

        size = (300, 300)
        or_image = Image.open(image_path)
        self.logo = ImageTk.PhotoImage(or_image.resize(size))
        main_label = ttk.Label(self.main_menu_frame, image=self.logo, background='#121212')
        main_label.grid(column=2, row=0, columnspan=2, pady=self.main_menu_frame.winfo_width()*0.15, sticky='s')

        cbutton('Add an User', 15, 2, 4, self.main_menu_frame, lambda: self.show_menu(self.side_menus.add_menu_frame))
        cbutton('Log-In', 15, 3, 4, self.main_menu_frame, lambda: self.show_menu(self.side_menus.login_menu_frame))