from main_package import Use
from main_package import NoteManagerGui
import os, json

try:
    with open(r'userdata\user.json', 'r') as f:
        data = json.load(f)
        Use.ulist = data
except (FileNotFoundError, json.JSONDecodeError):
    Use.lusers = []

os.system('cls')
app = NoteManagerGui()