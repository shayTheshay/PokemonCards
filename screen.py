import tkinter
from tkinter import *
from PIL import Image, ImageTk  
from data import *
 

# variables
base_color = "#008000"

# Create main window
root = Tk()
root.title("My First Memory Game")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg=base_color)

#Card variables
width = 150
height = 225

#iterate and print all the card states
for card in cardDeck:
    if card.orientation == "up":
        image = Image.open(card.image_front)
    else:
        image = Image.open(card.image_back)
    image = image.resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label = tkinter.Label(image=photo, bg = base_color)
    label.image = photo
    label.pack(pady=5)


# Run the GUI loop
root.mainloop()