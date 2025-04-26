from tkinter import ttk
from tkinter import *

def init_window():
    root = Tk()
    root.title("My First Memory Game")

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #color
    base_color = "#008000"
    root.geometry(f"{screen_width}x{screen_height}")

    style= ttk.Style()
    style.configure("Green.TFrame", background=base_color)
    mainframe = ttk.Frame(root, padding="3 3 12 12", style="Green.TFrame")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    
    return root, screen_width, screen_height, base_color, mainframe