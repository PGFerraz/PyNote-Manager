import os
import json
import shutil
import string
from tkinter import END, messagebox
from main_package.use_module import Use

def update_listbox(listbox):
    listbox.delete(0, END)
    for user in Use.ulist:
        listbox.insert(END, user['name'])

def validation(username_var, age_var, password_var, show_menu_func, main_menu_frame, update_listbox_func):
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
        show_menu_func()
        update_listbox_func()
    else:
        username_var.set('')
        age_var.set('')
        password_var.set('')

def remove_userGUI(listbox, password_var, status_label, ud_json, update_listbox_func):
    selected = listbox.curselection()
    if not selected:
        status_label.config(text="No user selected.", foreground="red")
        return

    name = listbox.get(selected[0])
    psw = password_var.get().strip()
    user = next((u for u in Use.ulist if u['name'].lower() == name.lower()), None)

    if not psw:
        status_label.config(text="Please enter a password.", foreground="red")
        return

    if user and user['password'] == psw:
        path = os.path.join('userdata', f'{name}_data')
        if os.path.isdir(path):
            try:
                shutil.rmtree(path)
            except Exception as e:
                status_label.config(text=f"Error removing folder: {e}", foreground="red")
                return

        Use.ulist = [u for u in Use.ulist if u["name"].lower() != name.lower()]
        update_listbox_func()

        try:
            with open(ud_json, 'r') as arq:
                dataj = json.load(arq)
            datajf = [d for d in dataj if d.get('name', '').lower() != name.lower()]
            with open(ud_json, 'w') as arq:
                json.dump(datajf, arq, indent=4)
        except Exception as e:
            status_label.config(text=f"Error updating JSON: {e}", foreground="red")
            return

        password_var.set('')
        status_label.config(text=f"User '{name}' removed successfully.", foreground="green")
    else:
        status_label.config(text="Authentication failed.", foreground="red")

def autentication(lusername_var, lpassword_var, show_profile_menu_func):
    name = lusername_var.get().strip()
    psw = lpassword_var.get().strip()

    if not name or not psw:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return
    if not Use.ulist:
        messagebox.showerror("Error", "No users registered.")
        return
    for user in Use.ulist:
        if user['name'] == name and user['password'] == psw:
            show_profile_menu_func(name)
            return
