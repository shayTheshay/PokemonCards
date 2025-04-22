from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk  
from data import *

# Create main window
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

#Card variables
width = int(screen_height/11*2)
height = int(screen_height/11*3)
padding_width = int((screen_width - width * 8 ) / 18)

#number of cards for screen 


def message_to_user(message:str):
    tkinter.messagebox.showinfo("Info",message)


def activate_screen():
    # variables
    #iterate and print all the card states
    for i, card in enumerate(cardDeck):
        if card.orientation == "face_up":
            image = Image.open(card.image_front)
        else:
            image = Image.open(card.image_back)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = tkinter.Label(mainframe, image=photo, bg = base_color)
        label.image = photo

        label.grid(row=i // 8, column=i % 8, padx=padding_width, pady=10)


    # Run the GUI loop
    root.mainloop()

