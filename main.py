from main_package import main_user_interface
from main_package import Use
import os, json

try:
    with open(r'userdata\user.json', 'r') as f:
        data = json.load(f)
        Use.ulist = data
except (FileNotFoundError, json.JSONDecodeError):
    Use.lusers = []

os.system('cls')
main_user_interface()