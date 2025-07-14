import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main_package.use_module import Use
from tkinter import *
from tkinter import ttk


class NoteManagerGui:
    def __init__(self):
        self.root = Tk()
        self.create_main_menu()
        self.create_addu_menu()
        self.create_remu_menu()
        self.show_menu(self.main_menu_frame)
        self.root.mainloop()
    
    def show_menu(self, frame): # Menu call function
        frame.tkraise()

    def create_addu_menu(self):
        # Add an User Menu

        # Main Frame
        self.add_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.add_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.add_menu_frame.rowconfigure(0, weight=1) # Seting Row and Column limit
        self.add_menu_frame.rowconfigure(10, weight=1)
        self.add_menu_frame.columnconfigure(0, weight=1)
        self.add_menu_frame.columnconfigure(10, weight=1)

        # Main Label
        add_label = ttk.Label(self.add_menu_frame, text="Add User Menu", style='Main_text.TLabel')
        add_label.grid(column=5, row=0, pady=10, sticky='n')
        # Username Entry Box Label
        add_uname_text = ttk.Label(self.add_menu_frame, text="Username:", style='Main_text.TLabel')
        add_uname_text.grid(column=5, row=1, pady=10, sticky='n')
        # Username Entry Box
        add_uname = ttk.Entry(self.add_menu_frame, textvariable='username', style='Custom.TEntry')
        add_uname.grid(column=5, row=2, sticky='n')
        # Password Entry Box Label
        add_upsw_text = ttk.Label(self.add_menu_frame, text="Password:", style='Main_text.TLabel')
        add_upsw_text.grid(column=5, row=3, pady=10, sticky='n')
        # Password Entry
        add_upsw = ttk.Entry(self.add_menu_frame, textvariable='password', style='Custom.TEntry')
        add_upsw.grid(column=5, row=4, sticky='n')

    def create_remu_menu(self):
        # Placeholder for remove menu creation
        pass


    def create_main_menu(self):
        # Setting Style Themes
        sty = ttk.Style()
        sty.theme_use('clam')
        sty.configure('dark_mode.TFrame', background='#2e2223', relief='raised')
        sty.configure('Main_text.TLabel', background='#2e2223', foreground='#ebd3d6', font=("Arial", 24, "bold"))
        sty.configure('Button_layout.TButton', background='#1c1515', foreground='#ebd3d6', font=("Arial", 24, "bold"), relief='raised')
        sty.configure('Custom.TEntry',
            foreground='#ebd3d6',
            fieldbackground='#1c1515',
            padding=5,
            font=('Arial', 14),
            relief='flat'
        )

        # Button Creator
        def cbutton(text, size, co, ro, funct):
            button = Button(self.main_menu_frame, 
                        text=f"{text}",
                        bg="#1c1515",
                        activebackground="#4a3938",
                        fg="#ebd3d6",
                        activeforeground="#ab6a72",
                        borderwidth=0,
                        width=20,
                        height=2,
                        command=funct, 
                        font=("Arial", int(size), "bold"),
                        relief='flat')    
            button.grid(column=co, row=ro, sticky='n')


        # Window Aspect
        self.root.geometry('800x600')
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)       

        # Background Frame
        self.main_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.main_menu_frame.rowconfigure(0, weight=1) # Seting Row and Column limit
        self.main_menu_frame.rowconfigure(10, weight=1)
        self.main_menu_frame.columnconfigure(0, weight=1)
        self.main_menu_frame.columnconfigure(10, weight=1)

        # Title Label
        main_label = ttk.Label(self.main_menu_frame, text="Note manager Gui", style='Main_text.TLabel')
        main_label.grid(column=5, row=0, pady=20, sticky='n')

        # Buttons
        button1 = cbutton('Add an User ➕', 12, 5, 1, lambda: self.show_menu(self.add_menu_frame))


app = NoteManagerGui()
