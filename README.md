# PyNote-Manager
<img width="322" height="266" alt="Image" src="https://github.com/user-attachments/assets/88f0cf82-4904-4b61-aaa8-d8625f697740" />

A simple and extensible Python application for creating and managing notes, with support for both command-line and graphical interfaces.
## Features

- ✅ User registration with secure password validation
- ❌ Remove users
- 🔐 Login system with authentication
- 🧾 Note creation, reading and deletion
- 💾 Notes stored per user in folders (JSON + .txt)
- 🖥️ GUI built with Tkinter
- 💻 Optional CLI (command-line interface)
- 🪶 Lightweight and easy to use
- 📂 Data stored in `.json` and `.txt` files

## Requirements
- Python 3.7 or higher
- pillow 11.3.0
- Works on Windows, Linux, and macOS (a terminal with Unicode support is recommended)

## Project Structure
MainFolder/
- main.py               # Launch the application (terminal mode)
- main_gui.py           # Launch the graphical user interface (GUI)
- assets/               # img files
- userdata/             # Stores user data and note files
- userdata/user.json    # Registered users list
- main_package/         # Core functionality modules
- main_package/__init__.py
- main_package/i_module.py         # Main interface and logic (terminal)
- main_package/use_module.py       # User class and data handling
- main_package/gui/                # GUI-related modules (Tkinter)
- main_package/gui/gui_main_module.py       # Main GUI window and menu
- main_package/gui/gui_main_side_module.py  # Side menus for user add, remove, login
- main_package/gui/gui_profile_module.py    # User profile menus
- main_package/gui/gui_utils.py             # Shared GUI utility functions
