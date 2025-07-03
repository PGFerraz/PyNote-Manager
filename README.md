# Terminal-note-Manager
A terminal-based note manager with multi-user support, login, and simple note creation/viewing.

## Features

- ✅ User registration with secure password validation
- 🔐 Login system with authentication
- 📝 Create personal notes
- 📖 View saved notes
- 🗑️ Delete notes
- ❌ Remove users
- 📂 Data stored in `.json` and `.txt` files

## Project Structure

MainFolder/
- main.py #launch the application
- userdata/ # Stores user data and note files
- userdata/user.json # Registered users list
- main_package/ # Core functionality modules
- mainpackage/__init__.py
- main_package/i_module.py # Main interface and logic
- main_package/use_module.py # User class and data handling
