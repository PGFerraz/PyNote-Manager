# Main file to launch the graphical interface
from main_package import Use
from main_package import NoteManagerGui
import os, json
ud_json = os.path.join('userdata', 'user.json')

# Load JSON file
try:
    with open(ud_json, 'r') as f:
        data = json.load(f)
        Use.ulist = data
except (FileNotFoundError, json.JSONDecodeError):
    Use.lusers = []
os.system('cls')

# Run GUI
app = NoteManagerGui()