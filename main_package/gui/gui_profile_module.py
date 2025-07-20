from tkinter import *
from tkinter import ttk
from main_package.gui.gui_utils import update_note_listbox
from tkinter.messagebox import *
from tkinter.filedialog import *

class GuiProfileMenus:
    def __init__(self, root, show_menu_callback, return_callback, tempu):
        self.root = root
        self.show_menu_callback = show_menu_callback
        self.return_callback = return_callback
        self.tempu = StringVar()
    # temp_user will be initialized in __init__ after root is set

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
    
    def show_profile_menu(self, name):
        self.create_profile_menu(name)
        self.profile_menu_frame.tkraise()

    def create_profile_menu(self, name):
        self.profile_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.profile_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.profile_menu_frame.rowconfigure(0, weight=1)
        self.profile_menu_frame.rowconfigure(10, weight=1)
        self.profile_menu_frame.columnconfigure(0, weight=1)
        self.profile_menu_frame.columnconfigure(10, weight=1)

        profile_label = ttk.Label(self.profile_menu_frame, text=f"{name} Profile Menu", style='Main_text.TLabel')
        profile_label.grid(column=5, row=0, pady=20, sticky='ns')

        view_button = self.cbutton('View Notes', 12, 5, 1, self.profile_menu_frame, lambda: [self.create_view_notes_menu(name), self.root.show_menu(self.view_notes_menu_frame)])
        view_button.grid(pady=10)

        ret_button = self.cbutton('Return', 12, 5, 2, self.profile_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)

    def create_view_notes_menu(self, name):
        self.view_notes_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.view_notes_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.view_notes_menu_frame.rowconfigure(0, weight=1)
        self.view_notes_menu_frame.rowconfigure(5, weight=1)
        self.view_notes_menu_frame.columnconfigure(0, weight=1)
        self.view_notes_menu_frame.columnconfigure(5, weight=1)
        view_label = ttk.Label(self.view_notes_menu_frame, text=f"{name} View Notes", style='Main_text.TLabel')
        view_label.grid(column=2, row=0, pady=20, sticky='we', columnspan=1, rowspan=1)

        self.listbox = Listbox(self.view_notes_menu_frame, height=10, width=40, background='#1c1515', foreground='#ebd3d6')
        self.listbox.grid(column=0, row=1, pady=0, padx=20, columnspan=3, rowspan=4)

        create_note_button = self.cbutton('Create a Note', 8, 4, 1, self.view_notes_menu_frame, lambda: print("nana"))
        create_note_button.grid(padx=2,columnspan=2, sticky='w')

        remove_note_button = self.cbutton('Remove a Note', 8, 4, 2, self.view_notes_menu_frame, lambda: print("nana"))
        remove_note_button.grid(padx=2,columnspan=2, sticky='w')

        edit_note_button = self.cbutton('Edit a Note', 8, 4, 3, self.view_notes_menu_frame, lambda: print("nana"))
        edit_note_button.grid(padx=2,columnspan=2, sticky='w')

        return_button = self.cbutton('Return', 8, 4, 4, self.view_notes_menu_frame, lambda: self.show_profile_menu(name))
        return_button.grid(padx=2,columnspan=2, sticky='w')
        update_note_listbox(self.listbox, name)