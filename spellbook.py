import runpy
from pynput import keyboard
import sqlite3
from tkinter import *
from tkinter import ttk
from time import sleep
import os

# Learn about dev chrome control, more general creation of folders and applying scripts in files with routing logic or manual folder creation with auto script finding



########## Tkinter Initialization Start ##########

#Create root
root = Tk()
root.title("Spellbook")
root.attributes("-topmost", 1)
root.overrideredirect(True)
root.geometry('600x200+700-49')

#Mainframe settings
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#Initialize
defaultKeys = 'asdfjkl;qweruiopzxcvm,./ghtybn'
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

withDraw = True
def toggle_menu():
    print('<ctrl>+<shift> pressed')
    global withDraw
    if(withDraw):
        root.withdraw()
        withDraw = False
    else:
        root.wm_deiconify()
        withDraw = True

def close_menu():
    global hotkeyListener
    print('<shift>+<esc> pressed')
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
    global currentDirectory
    global defaultKeys
    global menuLabel

    defaultKeyIndex = defaultKeys.find('{0}'.format(key.char))
    currentDirectory += '/' + os.listdir(currentDirectory)[defaultKeyIndex]
    currentDirectories = os.listdir(currentDirectory)
    dirLength = len(currentDirectories)
    newMenu = ''
    for i in range(dirLength):
        newMenu += defaultKeys[i] + '. ' + currentDirectories[i] + '\n'

    menuLabel.configure(text = newMenu)
    print('{0}'.format(key.char))
    print(newMenu)

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

########## Keypress Listener End ##########

root.mainloop()
"""
wizardDatabaseConnection = sqlite3.connect('wizard.db')
cursor = wizardDatabaseConnection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS spells (hotkey text, script text)')
cursor.execute('')
"""