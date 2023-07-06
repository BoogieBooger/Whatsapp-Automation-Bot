# Description: This is the main file for the program. It calls the GUI and the script files.
import gui
import tkinter as tk
import tkinter.font as tkFont




root = tk.Tk()
app = gui.App(root)
root.mainloop()