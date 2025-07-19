from main_package.use_module import Use
import os, json, shutil
from os import listdir

def top_menu(name, style):
    os.system('cls')
    menu_name = name
    bar_style = style
    for c in range(len(menu_name)+2): print(bar_style, end ='')
    print('\n',menu_name)
    for c in range(len(menu_name)+2): print(bar_style, end ='')
    
def autentication(username,psw):
    for user in Use.ulist:
        if user['name'] == username:
            if user['password'] == psw:
                return True

def create_note(user):
    while True:
        os.system('cls')
        top_menu('📝  Creating a Note', '=')
        content = ''
        arc_name = input('\n\nEnter Note Name -> ')
        arc_path = os.join.path('userdata', f'{user}_data', arc_name)
        os.system('cls')
        top_menu('Write the note in the field below. To exit type "exitnow" and press enter', '=')
        print('\n')
        while True:
            line = input()
            if line.strip().upper() == 'EXITNOW':
                break
            content += line + '\n'
            with open(arc_path, 'w', encoding='utf-8') as f:
                f.write(content)
        break
            
def show_notes(user):
    os.system('cls')
    notes_folder = os.path.join('userdata', f'{user}_data')
    top_menu('📖  Select a note to view', '=')
    print('\nNotes Found: ',*listdir(notes_folder), sep='\t')
    resp = input('\nEnter note name -> ')
    if resp in listdir(notes_folder):
        os.system('cls')
        top_menu(f'{resp}', '=')
        print('\n')
        resp_path = os.path.join('userdata', f'{user}_data', resp)
        f = open(resp_path, 'r', encoding='utf-8')
        print(f.read())
        input('Press enter to return to Profile Menu...')
    else:
        input(f'Note {resp} not found, press enter to return to Profile Menu...')

def delete_note(user):
    os.system('cls')
    notes_folder = os.path.join('userdata', f'{user}_data')
    top_menu('🗑️  Select a note to delete', '=')
    print('\nNotes Found: ',*listdir(notes_folder), sep='\t')
    resp = input('\nEnter note name -> ')
    resp_path = os.path.join(notes_folder, resp)
    if resp in listdir(notes_folder):
        os.remove(resp_path)
    else:
        input(f'Note {resp} not found, press enter to return to profile menu...')


def profile_interface(user):
    while True:
        os.system('cls')
        top_menu(f'👤  {user} Profile', '=')
        print(
            '\n\n1️⃣  📝  Create a Note'
            '\n2️⃣  📖  View Notes'
            '\n3️⃣  🗑️   Delete a Note'
            '\n4️⃣  🔙  Go back to main menu\n'
        )
        resp = str(input('Digit an option and press enter -> '))

        if resp == '1':
            create_note(user)
        elif resp == '2':
            show_notes(user)
        elif resp == '3':
            delete_note(user)           
        elif resp == '4':
            break

def remove_user():
    ud_json = os.path.join('userdata', 'user.json')
    while True:
        os.system('cls')
        top_menu('❌  Remove an User', '=')
        if not Use.ulist:
            input('\n\nNo users were found. Press Enter to return...')
            break
        print('\nUsers Found:')
        for users in Use.ulist:
            print(f"- {users['name']}", sep='\n')
        duser = input('\nEnter Username -> ').strip()
        dpsw = input('Enter Password -> ').strip()
        if autentication(duser, dpsw):
            resp = input(f'Are you sure to delete {duser}? (s/n) ').lower()
            if resp == 's':
                duser_lower = duser.lower()
                path = os.path.join('userdata', f'{duser}_data')
                # deleting user data folder
                if os.path.isdir(path):
                    try:
                        shutil.rmtree(path)
                        print(f"Folder {path} deleted.")
                    except Exception as e:
                        print(f"Error deleting folder {path}: {e}")
                # Update user list
                if any(d.get("name", "").lower() == duser_lower for d in Use.ulist):
                    Use.ulist = [d for d in Use.ulist if d.get("name", "").lower() != duser_lower]
                    # Updating JSON file
                    try:
                        with open(ud_json, 'r') as arq:
                            dataj = json.load(arq)
                        datajf = [d for d in dataj if d.get('name', '').lower() != duser_lower]
                        with open(ud_json, 'w') as arq:
                            json.dump(datajf, arq, indent=4)
                        print(f"User '{duser}' successfully removed.")
                    except Exception as e:
                        print(f"Error updating JSON file: {e}")
                else:
                    input('User Not Found. Press Enter to return...')
                    break
                input("Press Enter to continue...")
                break
            else:
                break
        else:
            resp2 = input('Authentication failed. Press Enter to try again, or enter "exit" to return...')
            lw = resp2.lower()
            if lw == 'exit':
                break

def main_user_interface():
    while True:
        top_menu('🗒️  Terminal note Manager by Pedro Ferraz', '=')
        print(
            '\n\n1️⃣  ➕ Add a User'
            '\n2️⃣  ❌ Remove a User'
            '\n3️⃣  👥 See all Users'
            '\n4️⃣  🔓 Login\n'
        )
        resp = str(input('Choose an option and press Enter -> '))

        if resp == '1':
            while True:
                os.system('cls')
                top_menu('Add a User ➕', '=')
                print('\n')
                Use.registration(self=Use)
                input('User added!! Press enter to return...')
                break
        elif resp == '2':
            remove_user()
            
        elif resp == '3':
            os.system('cls')
            top_menu('All Users 👥', '=')
            print('\n')
            Use.print_data(self=Use)
            input('\nPress enter to return...')
            
        elif resp == '4':
            while True:
                os.system('cls')
                top_menu('Log-in Screen 🔓', '=')
                print('\n')
                atmp_usr = input('Enter Your Username -> ')
                atmp_psw = input('Enter Your Password -> ')
                if autentication(atmp_usr, atmp_psw):
                    profile_interface(atmp_usr)
                else:
                    print('Username or Password incorrect...')
                    input('Press enter to return...')
                break