import os
import json
from main_package import Use
from main_package.gui.gui_utils import autentication2
from main_package.gui.gui_main_module import NoteManagerGui
from main_package.gui.gui_main_side_module import GuiMainSideMenus

ud_json = os.path.join('userdata', 'user.json')
tl_json = os.path.join('userdata', 'tl.json')

def load_json(path):
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None
    return None

# Load current logged user
ldata = load_json(tl_json)

# Load main user list
data = load_json(ud_json)
Use.ulist = data if data else []

os.system('cls' if os.name == 'nt' else 'clear')

# Start main app
if __name__ == '__main__':
    app = NoteManagerGui()
    
    if ldata and 'name' in ldata and 'psw' in ldata:
        # load the profile menu
        app.show_menu(app.side_menus.login_menu_frame)
        autentication2(ldata['name'], ldata['psw'], app.show_profile_menu(ldata['name']))
    else:
        # load the main menu
        app.show_menu(app.main_menu_frame)
    
    app.mainloop()
