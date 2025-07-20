# Main file to launch the terminal interface
from main_package.cli.i_module import main_user_interface
from main_package import Use
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

# Run in terminal
main_user_interface()