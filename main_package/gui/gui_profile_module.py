import os
from os import listdir
import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
from main_package.gui.gui_utils import update_note_listbox
from tkinter.messagebox import *
from tkinter import simpledialog

# Profile menu and submenus
class GuiProfileMenus:
    # getting data
    def __init__(self, root, show_menu_callback, return_callback, tempu):
        self.root = root
        self.show_menu_callback = show_menu_callback
        self.return_callback = return_callback
        self.path = StringVar()
        self.current_file_path = None

    # function to create buttons
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

    # Main profile menu
    def create_profile_menu(self, name):
        # initializing main frame
        self.profile_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.profile_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.profile_menu_frame.rowconfigure(0, weight=1)
        self.profile_menu_frame.rowconfigure(10, weight=1)
        self.profile_menu_frame.columnconfigure(0, weight=1)
        self.profile_menu_frame.columnconfigure(10, weight=1)

        # top label
        profile_label = ttk.Label(self.profile_menu_frame, text=f"{name} Profile Menu", style='Main_text.TLabel')
        profile_label.grid(column=5, row=0, pady=20, sticky='ns')

        # buttons
        # View user notes button
        view_button = self.cbutton('View Notes', 12, 5, 1, self.profile_menu_frame, lambda: [self.create_view_notes_menu(name), self.root.show_menu(self.view_notes_menu_frame)])
        view_button.grid(pady=10)
        # Return to main menu button
        ret_button = self.cbutton('Return', 12, 5, 2, self.profile_menu_frame, lambda: self.root.show_main_menu())
        ret_button.grid(pady=10)

    # read current file and display in editor
    def read_file(self, file_path):
        self.current_file_path = file_path
        self.text_area.delete('1.0', tk.END)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self.text_area.insert(tk.END, content)
    # Update the note files list
    def update_note_buttons(self, note_path):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()
        note_files = [f for f in os.listdir(note_path) if f.endswith('.txt')]
        for idx, file in enumerate(note_files):
            btn = Button(
                self.scroll_frame,
                text=file,
                width=15,
                font=("Sans", 10),
                bg="#1c1515", 
                fg="#ebd3d6",
                activebackground="#4a3938", 
                activeforeground="#ab6a72",
                command=lambda f=file: self.read_file(os.path.join(note_path, f)),
                relief='flat')
            btn.grid(row=idx, column=0, padx=18, pady=3, sticky='nsew')
    # function to change the directory of note files
    def change_dir(self):
        new_dir = filedialog.askdirectory()
        if new_dir:
            self.path.set(new_dir)
            self.update_note_buttons(new_dir)
            self.root.update()
    # popuo to create a new note
    def create_new_note(self):
        filename = simpledialog.askstring("New Note", "Enter the name of the note:")
        if filename:
            if not filename.endswith('.txt'):
                filename += '.txt'
            full_path = os.path.join(self.path.get(), filename)
            if os.path.exists(full_path):
                showwarning("Warning", "File already exists!")
                return
            with open(full_path, 'w') as f:
                f.write("")  # Cria arquivo vazio
            self.update_note_buttons(self.path.get())
            self.read_file(full_path)
    # save the currently selected note
    def save_current_note(self):
        if self.current_file_path:
            with open(self.current_file_path, 'w', encoding='utf-8') as f:
                f.write(self.text_area.get(1.0, tk.END))
            showinfo("Saved", "File saved successfully.")
        else:
            showwarning("Warning", "No file is currently opened.")
    # delete the currently selected note
    def delete_current_note(self):
        if self.current_file_path and os.path.exists(self.current_file_path):
            confirm = askyesno("Delete", f"Delete {os.path.basename(self.current_file_path)}?")
            if confirm:
                os.remove(self.current_file_path)
                self.current_file_path = None
                self.text_area.delete('1.0', tk.END)
                self.update_note_buttons(self.path.get())
        else:
            showwarning("Warning", "No file selected or file not found.")
    # menu for create, view, edit and remove notes 
    def create_view_notes_menu(self, name):
        self.path.set(os.path.join('userdata', f'{name}_main'))

        # initializing main frame
        self.view_notes_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.view_notes_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.view_notes_menu_frame.columnconfigure(0, weight=0)
        self.view_notes_menu_frame.columnconfigure(1, weight=0)
        self.view_notes_menu_frame.columnconfigure(2, weight=1)
        self.view_notes_menu_frame.rowconfigure(0, weight=0)
        self.view_notes_menu_frame.rowconfigure(1, weight=0)
        self.view_notes_menu_frame.rowconfigure(2, weight=1)

        # top label
        view_label = ttk.Label(
            self.view_notes_menu_frame,
            text=f"{name} View Notes",
            style='Main_text.TLabel'
        )
        view_label.grid(column=0, row=0, columnspan=3, pady=20, sticky='n')

        # buttons
        control_frame = ttk.Frame(self.view_notes_menu_frame, style='dark_mode.TFrame')
        control_frame.grid(row=1, column=0, columnspan=3, pady=10, sticky='n')
        self.cbutton('New Note', 8, 1, 1, control_frame, self.create_new_note).grid(padx=5, sticky='n')
        self.cbutton('Save Note', 8, 2, 1, control_frame, self.save_current_note).grid(padx=5, sticky='n')
        self.cbutton('Remove Note', 8, 3, 1, control_frame, self.delete_current_note).grid(padx=5, sticky='n')
        self.cbutton('Change Dir', 8, 4, 1, control_frame, self.change_dir).grid(padx=5, sticky='n')
        self.cbutton('Return', 8, 5, 1, control_frame, lambda: self.show_profile_menu(name)).grid(padx=5, sticky='n')

        # side file list
        canvas = tk.Canvas(self.view_notes_menu_frame, width=160, height=(self.root.winfo_height()*0.8), bg='#1c1515', highlightthickness=0)
        canvas.grid(row=2, column=0, sticky='ns', padx=(10, 0), pady=10)
        canvas.columnconfigure(2, weight=1)
        scrollbar = Scrollbar(self.view_notes_menu_frame, orient='vertical', command=canvas.yview)
        scrollbar.grid(row=2, column=1, sticky='ns', pady=10)
        canvas.configure(yscrollcommand=scrollbar.set)

        # files
        self.scroll_frame = ttk.Frame(canvas, style='BackgroundOnly.TEntry')
        canvas.create_window((0, 0), window=self.scroll_frame, anchor='nw')
        def on_frame_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        self.scroll_frame.bind('<Configure>', on_frame_configure)

        # Text edit area
        self.text_area = tk.Text(self.view_notes_menu_frame, wrap='word', width=50, font=("Sans", 10), height=25, bg='#1c1515', fg='#ebd3d6')
        self.text_area.grid(row=2, column=2, sticky='nsew', padx=(10, 20), pady=10)
        self.text_area.configure(padx=10, pady=10)

        # File buttons
        note_path = os.path.join('userdata', f'{name}_main')
        note_files = sorted([f for f in os.listdir(note_path) if f.endswith('.txt')])
        for idx, file in enumerate(note_files):
            btn = Button(
                self.scroll_frame,
                text=file,
                width=15,
                font=("Sans", 10),
                bg="#1c1515", 
                fg="#ebd3d6",
                activebackground="#4a3938", 
                activeforeground="#ab6a72",
                command=lambda f=file: self.read_file(os.path.join(note_path, f)),
                relief='flat'
            )
            btn.grid(row=idx, column=0, padx=18, pady=3, sticky='nsew')