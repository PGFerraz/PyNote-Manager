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

## Notes
- User passwords are currently stored in plain text (hashing coming soon).
- No external libraries are used — fully built with Python's standard library.
- This project was created as a way to practice and deepen my understanding of Python.
- It helped me explore concepts such as file handling, object-oriented programming, modularization, and terminal UI design.
