import string, os, time, json

class Use:

    dusers = {}
    ulist = []

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

    def registrationGUI(self, username, age, password):
        self.name = username
        self.age = age
        self.password = password

        Use.ulist.append({
            'name': self.name,
            'age': self.age,
            'password': self.password
        })

        os.makedirs(f'userdata/{self.name}_data', exist_ok=True)
        with open(f'userdata/{self.name}_data/{self.name}_main.txt', 'a') as f:
            f.write(f'User {self.name} registered at : {time.ctime()}\n'
                f'- Name : {self.name}\n'
                f'- Age : {self.age}\n')

        with open(f'userdata/user.json', 'w') as f:
            json.dump(Use.ulist, f, indent=4)

    def registration(self):
        self.name = input('Enter User Name -> ')
        self.age = input('Enter Your Age -> ')
        temp_menu = 'must contain a special character, a capital letter and a number!!'
        while True:
            os.system('cls')
            for c in range(len(temp_menu)+2): print('=', end ='')
            print(f'\nPassword Registration for user {self.name}')
            print('password must be at least 8 characters long!!')
            print('must contain a special character, a capital letter and a number!!')
            for c in range(len(temp_menu)+2): print('=', end ='')
            
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

        os.makedirs(f'userdata\{self.name}_data', exist_ok=True)
        with open(f'userdata\{self.name}_data\{self.name}_main.txt', 'a') as f:
            f.write(f'User {self.name} registered at : {time.ctime()}\n'
                    f'- Name : {self.name}\n'
                    f'- Age : {self.age}\n')

        with open(r'userdata\\user.json', 'w') as f:
            json.dump(Use.ulist, f, indent=4)

    def print_data(self):
        if not Use.ulist:
            print("No users found.")
            return

        for i, user in enumerate(Use.ulist, start=1):
            print(f'User {i}')
            print(f'  User Name : {user["name"]}')
            print(f'  User Age  : {user["age"]}\n')