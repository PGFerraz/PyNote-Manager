# Handles the creation and registration of user objects
import string, os, time, json, shutil

class Use:

    ulist = [] # List containing all currently registered users
    ud_json_path = os.path.join('userdata', 'user.json') # File path to the JSON file used to save registered users

    # Converts a dictionary into a User object
    @classmethod
    def from_dict(cls, data):
        user = cls()
        user.name = data['name']
        user.age = data['age']
        user.password = data['password']
        return user
    
    # User init vars
    def __init__(self):
        self.name = 'Not Given'
        self.age = 0
        self.password = 'Not'

    # Returns the directory and data file associated with a user
    # Using @staticmethod to prevent implicit 'self' argument
    @staticmethod
    def ud_main_folder_path(name):
        return os.path.join('userdata', f'{name}_main')
    @staticmethod
    def ud_main_txt_path(name):
        return os.path.join('userdata', f'{name}_main', f'{name}_data.txt')

    # Creates user directory, data file, and saves user object data to JSON
    def create_user_data(self):
        os.makedirs(self.ud_main_folder_path(self.name), exist_ok=True)
        with open(self.ud_main_txt_path(self.name), 'a') as f:
            f.write(f'User {self.name} registered at : {time.ctime()}\n'
                f'- Name : {self.name}\n'
                f'- Age : {self.age}\n')
        with open(self.ud_json_path, 'w') as f:
            json.dump(Use.ulist, f, indent=4)


    # User registration function for the graphical interface (gui_module.py)
    def registrationGUI(self, username, age, password):
        # Inputs obtained from gui_module
        self.name = username
        self.age = age
        self.password = password
        # Saving the current user to the user list "ulist"
        Use.ulist.append({
            'name': self.name,
            'age': self.age,
            'password': self.password
        })
        # Creating the user's directory and data file
        self.create_user_data()

    # User registration function for the terminal interface (i_module.py)
    def registration(self):
        self.name = input('Enter User Name -> ')
        self.age = input('Enter Your Age -> ')
        temp_name = self.name

        # setting password
        temp_menu = 'must contain a special character, a capital letter and a number!!'
        while True:
            os.system('cls')
            for c in range(len(temp_menu)+2): print('=', end ='')
            print(f'\nPassword Registration for user {self.name}')
            print('password must be at least 8 characters long!!')
            print('must contain a special character, a capital letter and a number!!')
            for c in range(len(temp_menu)+2): print('=', end ='')    
            temp_psw = input('\n\nType Password -> ')

            # Verifying whether the password meets the requirements
            if (
                any(char.isupper() for char in temp_psw) and
                any(char.isdigit() for char in temp_psw) and
                any(char in string.punctuation for char in temp_psw)
            ):
                self.password = temp_psw
                break
        # Saving the current user to the user list "ulist"
        Use.ulist.append({
            'name': self.name,
            'age': self.age,
            'password': self.password
        })
        # Creates the user directory and data file, then saves the object to JSON
        self.create_user_data(self)

    def print_data(self):
        if not Use.ulist:
            print("No users found.")
            return

        for i, user in enumerate(Use.ulist, start=1):
            print(f'User {i}')
            print(f'  User Name : {user["name"]}')
            print(f'  User Age  : {user["age"]}\n')