import sys, os, string, shutil, json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main_package.use_module import Use
from tkinter import *
from tkinter import ttk, messagebox, simpledialog


class NoteManagerGui:

    def __init__(self):
        self.root = Tk()
        self.create_main_menu()
        self.create_addu_menu()
        self.create_remo_menu()
        self.create_login_menu()
        self.temp_user = StringVar()
        self.show_menu(self.main_menu_frame)
        self.root.mainloop()
    # Menu call function

    def show_menu(self, frame):
        frame.tkraise()

    def show_profile_menu(self, name):
        self.temp_user = name
        self.create_profile_menu(name)
        self.show_menu(self.profile_menu_frame)

    # Button Creator
    def cbutton(self, text, size, co, ro, cframe, funct):
        button = Button(cframe, 
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
        return button

    def update_listbox(self):
        self.listbox.delete(0, END)
        for user in Use.ulist:
            self.listbox.insert(END, user['name'])

    def validation(self, username_var, age_var, password_var):
        username = username_var.get()
        age = age_var.get()
        password = password_var.get()
        if (
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in string.punctuation for char in password)
        ):
            Use().registrationGUI(username, age, password)
            username_var.set('')
            age_var.set('')
            password_var.set('')
            self.show_menu(self.main_menu_frame)
            self.update_listbox()
        else:
            username_var.set('')
            age_var.set('')
            password_var.set('')

    def create_addu_menu(self): # Add an User Menu
        # Main Frame
        self.add_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.add_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.add_menu_frame.rowconfigure(0, weight=1) # Seting Row and Column limit
        self.add_menu_frame.rowconfigure(10, weight=1)
        self.add_menu_frame.columnconfigure(0, weight=1)
        self.add_menu_frame.columnconfigure(10, weight=1)

        # Main Label
        add_label = ttk.Label(self.add_menu_frame, text="Add User Menu", style='Main_text.TLabel')
        add_label.grid(column=5, row=0, pady=20, sticky='ns')

        # Warning Label!
        add_label = ttk.Label(self.add_menu_frame,
            text="password must be at least 8 characters long!!\nmust contain a special character, a capital letter and a number!!", 
            anchor='center', justify='center',
            style='Main_text.TLabel', font=("Arial", 12, "bold"))
        add_label.grid(column=5, row=1, pady=0, sticky='n')

        # Username Entry Box Label
        add_uname_text = ttk.Label(self.add_menu_frame, text="Username:", style='Main_text.TLabel')
        add_uname_text.grid(column=5, row=2, pady=10, sticky='n')
        username_var = StringVar()
        add_uname = ttk.Entry(self.add_menu_frame, textvariable=username_var, style='Custom.TEntry')
        add_uname.grid(column=5, row=3, sticky='n')

        # Age Entry Box Label
        add_uage_text = ttk.Label(self.add_menu_frame, text="Age:", style='Main_text.TLabel')
        add_uage_text.grid(column=5, row=4, pady=10, sticky='n')
        age_var = StringVar()
        add_uage = ttk.Entry(self.add_menu_frame, textvariable=age_var, style='Custom.TEntry')
        add_uage.grid(column=5, row=5, sticky='n')

        # Password Entry Box Label
        add_upsw_text = ttk.Label(self.add_menu_frame, text="Password:", style='Main_text.TLabel')
        add_upsw_text.grid(column=5, row=6, pady=10, sticky='n')
        password_var = StringVar()
        add_upsw = ttk.Entry(self.add_menu_frame, textvariable=password_var, style='Custom.TEntry', show='*')
        add_upsw.grid(column=5, row=7, sticky='n')

        confirm_button = self.cbutton(
            "Confirm", 12, 5, 8, self.add_menu_frame,
            lambda: self.validation(username_var, age_var, password_var)
        )
        confirm_button.grid(pady=20)
        ret_button = self.cbutton('Return', 12, 5, 9, self.add_menu_frame, lambda: self.show_menu(self.main_menu_frame))
        ret_button.grid(pady=10)

    def remove_userGUI(self):
        selected = self.listbox.curselection()
        if not selected:
            self.status_label.config(text="No user selected.", foreground="red")
            return

        name = self.listbox.get(selected[0])
        psw = self.password_var.get().strip()

        user = next((u for u in Use.ulist if u['name'].lower() == name.lower()), None)

        if not psw:
            self.status_label.config(text="Please enter a password.", foreground="red")
            return

        if user and user['password'] == psw:
            # Confirmar remoção com botão/ação direta
            path = os.path.join('userdata', f'{name}_data')
            if os.path.isdir(path):
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    self.status_label.config(text=f"Error removing folder: {e}", foreground="red")
                    return

            Use.ulist = [u for u in Use.ulist if u["name"].lower() != name.lower()]
            self.update_listbox()

            try:
                with open(r'userdata/user.json', 'r') as arq:
                    dataj = json.load(arq)
                datajf = [d for d in dataj if d.get('name', '').lower() != name.lower()]
                with open(r'userdata/user.json', 'w') as arq:
                    json.dump(datajf, arq, indent=4)
            except Exception as e:
                self.status_label.config(text=f"Error updating JSON: {e}", foreground="red")
                return

            self.password_var.set('')
            self.status_label.config(text=f"User '{name}' removed successfully.", foreground="green")
        else:
            self.status_label.config(text="Authentication failed.", foreground="red")

    def create_remo_menu(self):
        self.remo_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.remo_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.remo_menu_frame.rowconfigure(0, weight=1)
        self.remo_menu_frame.rowconfigure(10, weight=1)
        self.remo_menu_frame.columnconfigure(0, weight=1)
        self.remo_menu_frame.columnconfigure(10, weight=1)

        # Título
        remo_label = ttk.Label(self.remo_menu_frame, text="Remove an User Menu", style='Main_text.TLabel')
        remo_label.grid(column=5, row=0, pady=20, sticky='ns')

        # Lista de usuários
        self.listbox = Listbox(self.remo_menu_frame, height=10, width=40, background='#1c1515', foreground='#ebd3d6')
        self.listbox.grid(column=5, row=1, pady=10)

        # Campo de senha
        self.password_var = StringVar()
        psw_label = ttk.Label(self.remo_menu_frame, text="Enter Password:", style='Main_text.TLabel')
        psw_label.grid(column=5, row=2, sticky='n')
        psw_entry = ttk.Entry(self.remo_menu_frame, textvariable=self.password_var, show='*', style='Custom.TEntry')
        psw_entry.grid(column=5, row=3, pady=5, sticky='n')

        # Mensagem de status
        self.status_label = ttk.Label(self.remo_menu_frame, text="", style='Main_text.TLabel', font=("Arial", 10, "bold"))
        self.status_label.grid(column=5, row=4, pady=10, sticky='n')

        # Botão de remoção

        ret_button = self.cbutton('Remove Selected', 12, 5, 5, self.remo_menu_frame, lambda: self.remove_userGUI())
        ret_button.grid(pady=10)
        ret_button = self.cbutton('Return', 12, 5, 6, self.remo_menu_frame, lambda: self.show_menu(self.main_menu_frame))
        ret_button.grid(pady=10)
        self.update_listbox()

    def autentication(self):

        name = self.lusername_var.get().strip()
        psw = self.lpassword_var.get().strip()

        if not name or not psw:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return
        if not Use.ulist:
            messagebox.showerror("Error", "No users registered.")
            return
        # Check if the user exists and the password matches
        for user in Use.ulist:
            if user['name'] ==  name:
                if user['password'] == psw:
                    self.show_profile_menu(name)
    
    def create_login_menu(self): # Add an User Menu
        # Main Frame
        self.login_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.login_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.login_menu_frame.rowconfigure(0, weight=1) # Seting Row and Column limit
        self.login_menu_frame.rowconfigure(10, weight=1)
        self.login_menu_frame.columnconfigure(0, weight=1)
        self.login_menu_frame.columnconfigure(10, weight=1)

        # Main Label
        login_label = ttk.Label(self.login_menu_frame, text="Log-In", style='Main_text.TLabel')
        login_label.grid(column=5, row=0, pady=20, sticky='ns')

        # Username Entry Box Label
        login_uname_text = ttk.Label(self.login_menu_frame, text="Username:", style='Main_text.TLabel')
        login_uname_text.grid(column=5, row=2, pady=10, sticky='n')
        self.lusername_var = StringVar()
        login_uname = ttk.Entry(self.login_menu_frame, textvariable=self.lusername_var, style='Custom.TEntry')
        login_uname.grid(column=5, row=3, sticky='n')
        
        # Password Entry Box Label
        login_upsw_text = ttk.Label(self.login_menu_frame, text="Password:", style='Main_text.TLabel')
        login_upsw_text.grid(column=5, row=6, pady=10, sticky='n')
        self.lpassword_var = StringVar()
        login_upsw = ttk.Entry(self.login_menu_frame, textvariable=self.lpassword_var, style='Custom.TEntry', show='*')
        login_upsw.grid(column=5, row=7, sticky='n')

        login_button = self.cbutton('Confirm', 12, 5, 8, self.login_menu_frame, lambda: self.autentication())
        login_button.grid(pady=10)
        ret_button = self.cbutton('Return', 12, 5, 9,self.login_menu_frame, lambda: self.show_menu(self.main_menu_frame))
        ret_button.grid(pady=10)

    def create_profile_menu(self, name): # Profile Menu
        self.profile_menu_frame = ttk.Frame(self.root, style='dark_mode.TFrame')
        self.profile_menu_frame.grid(row=0, column=0, sticky="nsew")
        self.profile_menu_frame.rowconfigure(0, weight=1)
        self.profile_menu_frame.rowconfigure(10, weight=1)
        self.profile_menu_frame.columnconfigure(0, weight=1)
        self.profile_menu_frame.columnconfigure(10, weight=1)

        # Title
        profile_label = ttk.Label(self.profile_menu_frame, text=f"{name} Profile Menu", style='Main_text.TLabel')
        profile_label.grid(column=5, row=0, pady=20, sticky='ns')

    

        # Update the listbox with current users
        self.update_listbox()


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
            relief='flat')

        # Window Aspect
        self.root.title('Note Manager by PGFerraz')
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
        button1 = self.cbutton('Add an User ➕', 12, 5, 1, self.main_menu_frame, lambda: self.show_menu(self.add_menu_frame))
        button1.grid(pady=10)
        button2 = self.cbutton('Remove a User ❌', 12, 5, 2, self.main_menu_frame, lambda: self.show_menu(self.remo_menu_frame))
        button2.grid(pady=10)
        button3 = self.cbutton('Log-In', 12, 5, 3, self.main_menu_frame, lambda: self.show_menu(self.login_menu_frame))
        button3.grid(pady=10)