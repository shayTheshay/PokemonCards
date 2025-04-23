from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk  
from data import *
from data import cardPokemon

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
padding_height = int((screen_height - height * 3 ) / 15)

#photo_refs = []

#number of cards for screen 
number_of_rows = 3
number_of_columns = 8

cardDeck = fixed_pokemon_deck(cardDeck, number_of_rows, number_of_columns)


tmp_card = []
cards_face_up = []
two_cards = 0

def on_card_click(card, label):
    global two_cards, cards_face_up, tmp_card

    if card in cards_face_up or card in tmp_card:
        return
        
    card.change_orientation()
    img_path = card.image_front if card.orientation == "face_up" else card.image_back
    image = Image.open(img_path).resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    #photo_refs.append(photo)

    tmp_card.append((card, label))
    two_cards += 1
    if two_cards == 2:
        two_cards = 0
        print(two_cards)
        if tmp_card[0].id == tmp_card[1].id:
            cards_face_up.append(tmp_card[0])
            cards_face_up.append(tmp_card[1])
            tmp_card.clear()
           

                

    

            


def message_to_user(message:str):
    tkinter.messagebox.showinfo("Info",message)


def activate_screen():
    # variables
    #iterate and print all the card states
    randomize_deck(cardDeck)

    for i, card in enumerate(cardDeck):
        if card.orientation == "face_up":
            image = Image.open(card.image_front)
        else:
            image = Image.open(card.image_back)
        image = image.resize((width, height))
        photo = ImageTk.PhotoImage(image)
        label = tkinter.Label(mainframe, image=photo, bg = base_color)
        label.image = photo

        label.bind("<Button-1>", lambda e, c=card, l=label: on_card_click(c, l))

        label.grid(row=i // 8, column=i % 8, padx=padding_width, pady=padding_height)


    # Run the GUI loop
    root.mainloop()

