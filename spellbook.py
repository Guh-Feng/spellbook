import runpy
from pynput import keyboard
import sqlite3
from tkinter import *
from tkinter import ttk
from time import sleep
from pynput import keyboard

#Create root
root = Tk()
root.title("Tracking App")
root.attributes("-topmost", 1)

#Mainframe settings
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Spell Book').grid(column=1, row=1)
ttk.Label(mainframe, text='A. Automation Script\nS. Pasting Templates\nD. Opening Stuff\nF. API Access').grid(column=1, row=2)
# Learn about dev chrome control, more general creation of folders and applying scripts in files with routing logic or manual folder creation with auto script finding
# ttk.Label(mainframe, text='Col 2').grid(column=2, row=2)
# ttk.Label(mainframe, text='Col 3').grid(column=3, row=2)

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
    global listener
    print('<esc> pressed')
    listener.stop()
    root.destroy()

listener = keyboard.GlobalHotKeys({
        '<ctrl>+<shift>': toggle_menu,
        '<esc>': close_menu})
listener.start()

root.mainloop()
"""
wizardDatabaseConnection = sqlite3.connect('wizard.db')
cursor = wizardDatabaseConnection.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS spells (hotkey text, script text)')
cursor.execute('')
"""