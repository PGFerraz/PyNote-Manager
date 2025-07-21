import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from main_package.use_module import Use
from main_package.gui.gui_utils import update_listbox, validation, remove_userGUI, autentication, cbutton

class GuiMainSideMenus():
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.create_addu_menu()
        self.create_login_menu()

    def show_profile_menu(self, name):
        self.create_profile_menu(name)
        self.profile_menu_frame.tkraise()

    # Add User Menu
    def create_addu_menu(self):
        self.add_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.add_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.add_menu_frame.rowconfigure(0, weight=1)
        self.add_menu_frame.rowconfigure(5, weight=1)
        self.add_menu_frame.columnconfigure(0, weight=1)
        self.add_menu_frame.columnconfigure(5, weight=1)

        add_label = ttk.Label(self.add_menu_frame, text="Add User Menu", style='Main_text.TLabel')
        add_label.grid(column=3, row=0, pady=20, sticky='ns')

        # add_label2 = ttk.Label(self.add_menu_frame,
        #     text="Password must be at least 8 characters long!\nMust contain a special character, a capital letter and a number!",
        #     anchor='center', justify='center',
        #     style='Main_text.TLabel', font=("Arial", 12, "bold"))
        # add_label2.grid(column=5, row=1, pady=0, sticky='n')

        add_uname_text = ttk.Label(self.add_menu_frame, text="Username ", style='Sub_text.TLabel')
        add_uname_text.grid(column=2, row=2, pady=5, sticky='e')
        self.username_var = StringVar()
        add_uname = ttk.Entry(self.add_menu_frame, textvariable=self.username_var, style='Custom.TEntry')
        add_uname.grid(column=3, row=2)

        add_uage_text = ttk.Label(self.add_menu_frame, text="Age ", style='Sub_text.TLabel')
        add_uage_text.grid(column=2, row=3, pady=5, sticky='e')
        self.age_var = StringVar()
        add_uage = ttk.Entry(self.add_menu_frame, textvariable=self.age_var, style='Custom.TEntry')
        add_uage.grid(column=3, row=3)

        add_upsw_text = ttk.Label(self.add_menu_frame, text="Password ", style='Sub_text.TLabel')
        add_upsw_text.grid(column=2, row=4, pady=5, sticky='e')
        self.password_var = StringVar()
        add_upsw = ttk.Entry(self.add_menu_frame, textvariable=self.password_var, style='Custom.TEntry', show='*')
        add_upsw.grid(column=3, row=4)

        confirm_button = cbutton(
            "Confirm", 7, 2, 5, self.add_menu_frame,
            lambda: validation(
                self.username_var,
                self.age_var,
                self.password_var,
                self.root.show_main_menu,
                self.root.main_menu_frame,
                lambda: update_listbox(self.listbox)
            ), 'medium'
        )
        confirm_button.grid(pady=20)

        ret_button = cbutton('Return', 12, 4, 5, self.add_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)

    # Login Menu
    def create_login_menu(self):
        self.login_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.login_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.login_menu_frame.rowconfigure(0, weight=1)
        self.login_menu_frame.rowconfigure(10, weight=1)
        self.login_menu_frame.columnconfigure(0, weight=1)
        self.login_menu_frame.columnconfigure(10, weight=1)

        login_label = ttk.Label(self.login_menu_frame, text="Log-In", style='Main_text.TLabel')
        login_label.grid(column=5, row=0, pady=20, sticky='ns')

        login_uname_text = ttk.Label(self.login_menu_frame, text="Username:", style='Main_text.TLabel')
        login_uname_text.grid(column=5, row=2, pady=10, sticky='n')
        self.lusername_var = StringVar()
        login_uname = ttk.Entry(self.login_menu_frame, textvariable=self.lusername_var, style='Custom.TEntry')
        login_uname.grid(column=5, row=3, sticky='n')

        login_upsw_text = ttk.Label(self.login_menu_frame, text="Password:", style='Main_text.TLabel')
        login_upsw_text.grid(column=5, row=6, pady=10, sticky='n')
        self.lpassword_var = StringVar()
        login_upsw = ttk.Entry(self.login_menu_frame, textvariable=self.lpassword_var, style='Custom.TEntry', show='*')
        login_upsw.grid(column=5, row=7, sticky='n')

        login_button = cbutton('Confirm', 12, 5, 8, self.login_menu_frame,
                                    lambda: autentication(self.lusername_var, self.lpassword_var, self.root.show_profile_menu))
        login_button.grid(pady=10)

        ret_button = cbutton('Return', 12, 5, 9, self.login_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)
