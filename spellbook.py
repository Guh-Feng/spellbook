import runpy
from pynput import keyboard
import sqlite3
from tkinter import *
from tkinter import ttk
from time import sleep
import os

import sv_ttk

# Learn about dev chrome control, more general creation of folders and applying scripts in files with routing logic or manual folder creation with auto script finding
# Outside scripts return 0, configures scripts to run, have the window work and scripts run when not withdrawn


########## Tkinter Initialization Start ##########

#Create root
root = Tk()
root.title("Spellbook")
root.attributes("-topmost", 1)
root.geometry('600x150+700-49')

#Mainframe settings
mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.place(relx=0.5, rely=0.5, anchor=CENTER)

#Initialize
defaultKeys = 'asdfjkl;qweruiopzxcvm,./ghtybn'
rootDirectory = './spells (scripts)'
currentDirectory = './spells (scripts)'

directories = os.listdir(currentDirectory)
dirLength = len(directories)
menu = ''
for i in range(dirLength):
    menu += defaultKeys[i] + '. ' + directories[i] + '\n'

# title = ttk.Label(mainframe, text='Spellbook')
# title.grid(column=1, row=1, sticky=(W, E))
menuLabel = ttk.Label(mainframe, text=menu)
menuLabel.grid(column=1, row=2, sticky=(W, E))

########## Tkinter Initialization End ##########



########## Hotkey Listener Start ##########

withDrawn = False
def toggle_menu():
    # print('<ctrl>+<shift> pressed')
    global withDrawn
    if(withDrawn):
        root.deiconify()
        withDrawn = False
    else:
        root.withdraw()
        withDrawn = True

def close_menu():
    global hotkeyListener
    # print('<shift>+<esc> pressed')
    hotkeyListener.stop()
    root.destroy()

hotkeyListener = keyboard.GlobalHotKeys({
        '<ctrl>+<shift>': toggle_menu,
        '<shift>+<esc>': close_menu})
hotkeyListener.start()

########## Hotkey Listener End ##########



########## Keypress Listener Start ##########

keypressListener = keyboard.Listener()

def on_press(key):
    #No actions when withdrawn
    global withDrawn
    # print(withDrawn)
    if(withDrawn):
       return 

    global currentDirectory
    global defaultKeys
    global menuLabel
    global rootDirectory

    #Entering scopes
    try:
        defaultKeyIndex = defaultKeys.find('{0}'.format(key.char))
        currentDirectory += '/' + os.listdir(currentDirectory)[defaultKeyIndex]

        if('.py' in currentDirectory):
            runpy.run_path(currentDirectory)
        
        currentDirectories = os.listdir(currentDirectory)
        dirLength = len(currentDirectories)
        newMenu = ''

        for i in range(dirLength):
            newMenu += defaultKeys[i] + '. ' + currentDirectories[i] + '\n'

        menuLabel.configure(text = newMenu)

    #Exiting scopes
    except AttributeError:
        if(key == keyboard.Key.tab):
            currentDirectory = currentDirectory[0:currentDirectory.rfind('/')]
            currentDirectories = os.listdir(currentDirectory)
            dirLength = len(currentDirectories)
            newMenu = ''

            for i in range(dirLength):
                newMenu += defaultKeys[i] + '. ' + currentDirectories[i] + '\n'

            menuLabel.configure(text = newMenu)
        if(key == keyboard.Key.esc):
            currentDirectory = rootDirectory
            currentDirectories = os.listdir(currentDirectory)
            dirLength = len(currentDirectories)
            newMenu = ''

            for i in range(dirLength):
                newMenu += defaultKeys[i] + '. ' + currentDirectories[i] + '\n'

            menuLabel.configure(text = newMenu)
 

    except NotADirectoryError:
        currentDirectory = rootDirectory
        currentDirectories = os.listdir(currentDirectory)
        dirLength = len(currentDirectories)
        newMenu = ''

        for i in range(dirLength):
            newMenu += defaultKeys[i] + '. ' + currentDirectories[i] + '\n'

        menuLabel.configure(text = newMenu)
        toggle_menu()
    
    except IndexError:
        return

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

########## Keypress Listener End ##########

sv_ttk.set_theme("dark")

root.mainloop()
"""
wizardDatabaseConnection = sqlite3.connect('wizard.db')
cursor = wizardDatabaseConnection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS spells (hotkey text, script text)')
cursor.execute('')
"""