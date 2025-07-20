import os
from tkinter import *
from tkinter import ttk
from main_package.use_module import Use
from main_package.gui.gui_utils import update_listbox, validation, remove_userGUI, autentication

class GuiMainSideMenus():
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.create_addu_menu()
        self.create_remo_menu()
        self.create_login_menu()

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

    # Add User Menu
    def create_addu_menu(self):
        self.add_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.add_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.add_menu_frame.rowconfigure(0, weight=1)
        self.add_menu_frame.rowconfigure(10, weight=1)
        self.add_menu_frame.columnconfigure(0, weight=1)
        self.add_menu_frame.columnconfigure(10, weight=1)

        add_label = ttk.Label(self.add_menu_frame, text="Add User Menu", style='Main_text.TLabel')
        add_label.grid(column=5, row=0, pady=20, sticky='ns')

        add_label2 = ttk.Label(self.add_menu_frame,
            text="Password must be at least 8 characters long!\nMust contain a special character, a capital letter and a number!",
            anchor='center', justify='center',
            style='Main_text.TLabel', font=("Arial", 12, "bold"))
        add_label2.grid(column=5, row=1, pady=0, sticky='n')

        add_uname_text = ttk.Label(self.add_menu_frame, text="Username:", style='Main_text.TLabel')
        add_uname_text.grid(column=5, row=2, pady=10, sticky='n')
        self.username_var = StringVar()
        add_uname = ttk.Entry(self.add_menu_frame, textvariable=self.username_var, style='Custom.TEntry')
        add_uname.grid(column=5, row=3, sticky='n')

        add_uage_text = ttk.Label(self.add_menu_frame, text="Age:", style='Main_text.TLabel')
        add_uage_text.grid(column=5, row=4, pady=10, sticky='n')
        self.age_var = StringVar()
        add_uage = ttk.Entry(self.add_menu_frame, textvariable=self.age_var, style='Custom.TEntry')
        add_uage.grid(column=5, row=5, sticky='n')

        add_upsw_text = ttk.Label(self.add_menu_frame, text="Password:", style='Main_text.TLabel')
        add_upsw_text.grid(column=5, row=6, pady=10, sticky='n')
        self.password_var = StringVar()
        add_upsw = ttk.Entry(self.add_menu_frame, textvariable=self.password_var, style='Custom.TEntry', show='*')
        add_upsw.grid(column=5, row=7, sticky='n')

        confirm_button = self.cbutton(
            "Confirm", 12, 5, 8, self.add_menu_frame,
            lambda: validation(
                self.username_var,
                self.age_var,
                self.password_var,
                self.root.show_main_menu,
                self.root.main_menu_frame,
                lambda: update_listbox(self.listbox)
            )
        )
        confirm_button.grid(pady=20)

        ret_button = self.cbutton('Return', 12, 5, 9, self.add_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)

    # Remove User Menu
    def create_remo_menu(self):
        self.remo_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.remo_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.remo_menu_frame.rowconfigure(0, weight=1)
        self.remo_menu_frame.rowconfigure(10, weight=1)
        self.remo_menu_frame.columnconfigure(0, weight=1)
        self.remo_menu_frame.columnconfigure(10, weight=1)

        remo_label = ttk.Label(self.remo_menu_frame, text="Remove User Menu", style='Main_text.TLabel')
        remo_label.grid(column=5, row=0, pady=20, sticky='ns')

        self.listbox = Listbox(self.remo_menu_frame, height=10, width=40, background='#1c1515', foreground='#ebd3d6')
        self.listbox.grid(column=5, row=1, pady=10)

        self.password_var_remove = StringVar()
        psw_label = ttk.Label(self.remo_menu_frame, text="Enter Password:", style='Main_text.TLabel')
        psw_label.grid(column=5, row=2, sticky='n')
        psw_entry = ttk.Entry(self.remo_menu_frame, textvariable=self.password_var_remove, show='*', style='Custom.TEntry')
        psw_entry.grid(column=5, row=3, pady=5, sticky='n')

        self.status_label = ttk.Label(self.remo_menu_frame, text="", style='Main_text.TLabel', font=("Arial", 10, "bold"))
        self.status_label.grid(column=5, row=4, pady=10, sticky='n')

        remo_button = self.cbutton('Remove Selected', 12, 5, 5, self.remo_menu_frame, lambda: remove_userGUI(
            self.listbox,
            self.password_var_remove,
            self.status_label,
            self.root.ud_json,
            lambda: update_listbox(self.listbox)
        ))
        remo_button.grid(pady=10)

        ret_button = self.cbutton('Return', 12, 5, 6, self.remo_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)

        update_listbox(self.listbox)

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

        login_button = self.cbutton('Confirm', 12, 5, 8, self.login_menu_frame,
                                    lambda: autentication(self.lusername_var, self.lpassword_var, self.root.show_profile_menu))
        login_button.grid(pady=10)

        ret_button = self.cbutton('Return', 12, 5, 9, self.login_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)
