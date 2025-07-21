# Main file to launch the GUI interface
import os
import json
from main_package import Use
from main_package.gui.gui_main_module import NoteManagerGui

ud_json = os.path.join('userdata', 'user.json')

# Load JSON file
try:
    with open(ud_json, 'r') as f:
        data = json.load(f)
        Use.ulist = data
except (FileNotFoundError, json.JSONDecodeError):
    Use.ulist = []

os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    app = NoteManagerGui()
    app.mainloop()