import string
import os
import time
import json

class Use:

    ulist = []  # List containing all currently registered users
    ud_json_path = os.path.join('userdata', 'user.json')  # Path to JSON file

    @classmethod
    def from_dict(cls, data):
        user = cls()
        user.name = data['name']
        user.age = data['age']
        user.password = data['password']
        return user

    def __init__(self):
        self.name = 'Not Given'
        self.age = 0
        self.password = 'Not'

    @staticmethod
    def ud_main_folder_path(name):
        return os.path.join('userdata', f'{name}_main')

    @staticmethod
    def ud_main_txt_path(name):
        return os.path.join('userdata', f'{name}_main', f'{name}_data.txt')

    def create_user_data(self):
        os.makedirs(self.ud_main_folder_path(self.name), exist_ok=True)
        with open(self.ud_main_txt_path(self.name), 'a') as f:
            f.write(f'User {self.name} registered at : {time.ctime()}\n'
                    f'- Name : {self.name}\n'
                    f'- Age : {self.age}\n')
        with open(self.ud_json_path, 'w') as f:
            json.dump(Use.ulist, f, indent=4)

    def registrationGUI(self, username, age, password):
        self.name = username
        self.age = age
        self.password = password
        Use.ulist.append({
            'name': self.name,
            'age': self.age,
            'password': self.password
        })
        self.create_user_data()

    def registration(self):
        self.name = input('Enter User Name -> ')
        self.age = input('Enter Your Age -> ')
        temp_menu = 'must contain a special character, a capital letter and a number!!'
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('=' * (len(temp_menu)+2))
            print(f'\nPassword Registration for user {self.name}')
            print('password must be at least 8 characters long!!')
            print('must contain a special character, a capital letter and a number!!')
            print('=' * (len(temp_menu)+2))
            temp_psw = input('\n\nType Password -> ')
            if (
                any(char.isupper() for char in temp_psw) and
                any(char.isdigit() for char in temp_psw) and
                any(char in string.punctuation for char in temp_psw)
            ):
                self.password = temp_psw
                break
        Use.ulist.append({
            'name': self.name,
            'age': self.age,
            'password': self.password
        })
        self.create_user_data()

    def print_data(self):
        if not Use.ulist:
            print("No users found.")
            return
        for i, user in enumerate(Use.ulist, start=1):
            print(f'User {i}')
            print(f'  User Name : {user["name"]}')
            print(f'  User Age  : {user["age"]}\n')