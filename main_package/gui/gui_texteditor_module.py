import tkinter 
import os 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class TextEditor():
    # Protected Vars 
    __textEditorRoot = Tk()
    __defautWindowWidth = 800
    __defautWindowHeight = 600
    __defautTextEditArea = Text(__textEditorRoot)
    __defautMenuBar = Menu(__textEditorRoot)
    __optionFileMenu = Menu(__defautMenuBar, tearoff=0)
    __optionEditMenu = Menu(__defautMenuBar, tearoff=0)
    __optionHelpMenu = Menu(__defautMenuBar, tearoff=0)
    __featureScrollBar = Scrollbar(__defautTextEditArea)     
    __file = None

    def __init__(self, **kwargs):
        # Setting window size
        try:
            self.__defautWindowWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__defautWindowHeight = kwargs['height']
        except KeyError:
            pass

        self.__textEditorRoot.title("Untitled Note - Pynote Manager")
        # Center the window
        screenWidth = self.__textEditorRoot.winfo_screenwidth()
        screenHeight = self.__textEditorRoot.winfo_screenheight()
        # Window left-align
        left = (screenWidth / 2) - (self.__defautWindowWidth / 2) 
        # Window right-align
        top = (screenHeight / 2) - (self.__defautWindowHeight /2) 
        # For top and bottom
        self.__textEditorRoot.geometry('%dx%d+%d+%d' % (self.__defautWindowWidth,
                                              self.__defautWindowHeight,
                                              left, top)) 
        # Auto resizing the text area
        self.__textEditorRoot.grid_rowconfigure(0, weight=1)
        self.__textEditorRoot.grid_columnconfigure(0, weight=1)
        # Add controls (widget)
        self.__defautTextEditArea.grid(sticky = N + E + S + W)
        
        # "File" menu in top menu bar
        # Option to open new file
        self.__optionFileMenu.add_command(label="New",
                                        command=self.__newFile)    
        # Option to save current file
        self.__optionFileMenu.add_command(label="Save",
                                        command=self.__saveFile)    
        # To create a line in the dialog        
        self.__optionFileMenu.add_separator()                                         
        self.__optionFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__defautMenuBar.add_cascade(label="File",
                                       menu=self.__optionFileMenu)     
        # To give a feature of cut 
        self.__optionEditMenu.add_command(label="Cut",
                                        command=self.__cut)             
        # to give a feature of copy    
        self.__optionEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
        # To give a feature of paste
        self.__optionEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
        # To give a feature of editing
        self.__defautMenuBar.add_cascade(label="Edit",
                                       menu=self.__optionEditMenu)     
        # To create a feature of description of the notepad
        self.__optionHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout) 
        self.__defautMenuBar.add_cascade(label="Help",
                                       menu=self.__optionHelpMenu)
        self.__textEditorRoot.config(menu=self.__defautMenuBar)

        # Setting Scrollbar
        self.__featureScrollBar.pack(side=RIGHT,fill=Y)                           
        self.__featureScrollBar.config(command=self.__defautTextEditArea.yview)     
        self.__defautTextEditArea.config(yscrollcommand=self.__featureScrollBar.set)
    
        
    def __quitApplication(self):
        self.__textEditorRoot.destroy()
        # exit()
    def __showAbout(self):
        showinfo("PyNote - Manager","PGferraz")
    # New file option
    def __newFile(self):
        self.__textEditorRoot.title("Untitled - Notepad")
        self.__file = None
        self.__defautTextEditArea.delete(1.0,END)
    # Save file option
    def __saveFile(self):
        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
            if self.__file == "":
                self.__file = None
            else:
                # Saving the current file
                file = open(self.__file,"w")
                file.write(self.__defautTextEditArea.get(1.0,END))
                file.close()
                # Change the window title to the file name
                self.__textEditorRoot.title(os.path.basename(self.__file) + " - Notepad")
        else:
            file = open(self.__file,"w")
            file.write(self.__defautTextEditArea.get(1.0,END))
            file.close()
    def __cut(self):
        self.__defautTextEditArea.event_generate("<<Cut>>")
    def __copy(self):
        self.__defautTextEditArea.event_generate("<<Copy>>")
    def __paste(self):
        self.__defautTextEditArea.event_generate("<<Paste>>")

    def run(self):
        self.__defautTextEditArea.mainloop()
# Run main application
notepad = TextEditor(width=600,height=400)
notepad.run()