import os
import json
import shutil
import string
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import END, messagebox
from main_package.use_module import Use
from os import listdir

_custom_main_menu_logo_path = os.path.join('assets','img', 'custom_main_menu_logo_v1.png')
_custom_button_image_path = os.path.join('assets','img', 'custom_button_v1.png')
_custom_button_msize_image_path = os.path.join('assets', 'img', 'custom_button_v1_msize.png')
loaded_images = []

# Buton Creator
def cbutton(text, size, co, ro, cframe, funct, bsize=None, custom_button_image_path=_custom_button_image_path):
    if bsize == 'medium':
        custom_button_image_path = _custom_button_msize_image_path

    custom_button_image = tk.PhotoImage(file=custom_button_image_path)
    loaded_images.append(custom_button_image)

    button = tk.Button(
        cframe,
        text=text,
        image=custom_button_image,
        compound="center",
        bg="#121212", fg="#ebd3d6",
        activebackground="#121212", activeforeground="#ab6a72",
        borderwidth=0, width=256, height=144,
        command=funct,
        font=("Segoe UI", int(size), "bold"),
        relief='flat'
    )
    button.grid(column=co, row=ro, sticky='n')
    return button

def update_listbox(listbox):
    listbox.delete(0, END)
    for user in Use.ulist:
        listbox.insert(END, user['name'])

def update_note_listbox(listbox, name):
    notes_folder = os.path.join('userdata', f'{name}_main')
    listbox.delete(0, END)
    for note in listdir(notes_folder):
        listbox.insert(END, note)
        
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
    tempLoginPath = os.path.join('userdata', 'tl.json')
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
            Use.temp_login.append({'name': name, 'psw': psw})
            with open(tempLoginPath, 'w') as f:
                json.dump(Use.temp_login, f, indent=4)
            show_profile_menu_func(name)
            print(name)
            return

def autentication2(lusername_var, lpassword_var, show_profile_menu_func):
    name = lusername_var
    psw = lpassword_var
    for user in Use.ulist:
        if user['name'] == name and user['password'] == psw:
            show_profile_menu_func(name)
            return