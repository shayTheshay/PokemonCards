from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk  
from data import *
from data import cardPokemon


#CR: main logic in seperate file - in logic file

#number of cards for screen 
number_of_rows = 3
number_of_columns = 8

cardDeck = fixed_pokemon_deck(cardDeck, number_of_rows, number_of_columns)

tmp_card = []
cards_face_up = []
num_of_moves = 0

def change_card_image(card:cardPokemon, label:tkinter.Label, width, height):
    card.change_orientation()
    img_path = card.image_front if card.orientation == "face_up" else card.image_back
    image = Image.open(img_path).resize((width, height))
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo


#CR: simplify, move some to functions
def on_card_click(card:cardPokemon, label:tkinter.Label, width, height, root): 
    global cards_face_up, tmp_card, num_of_moves
    num_of_moves += 1
    #CR: use less if in if
    if (card, label) in cards_face_up:
        return
    
    # if (card, label) not in cards_face_up:
    if (card, label) in tmp_card and card.orientation == "face_up":
        change_card_image(card, label, width, height)
        tmp_card.remove((card, label))
        return

    tmp_card.append((card, label))
    change_card_image(card, label, width, height)
    label.update_idletasks()

    if len(tmp_card) == 2:
        #CR: move to function, single responsibility 
        def evaluate_match(card:cardPokemon, label:tkinter.Label):
            if tmp_card[0][0] == tmp_card[1][0]:
                if card.orientation != "face_up":
                    change_card_image(card, label, width, height)
                for ((card, label)) in tmp_card:
                    cards_face_up.append((card, label))
            else:
                for ((card, label)) in tmp_card:
                    root.after(300, change_card_image(card, label, width, height))                
            tmp_card.clear()
        root.after(0, evaluate_match(card, label))
            
    if(len(cards_face_up) == number_of_rows * number_of_columns):
        message_to_user("YOU Won! to play again please close and open again the program")    

def message_to_user(message:str):
    tkinter.messagebox.showinfo("Info",message)


def activate_screen(root, screen_width, screen_height, base_color, mainframe):
    # variables
    width = int(screen_height/11*2)
    height = int(screen_height/11*3)
    padding_width = int((screen_width - width * 8 ) / 18)
    padding_height = int((screen_height - height * 3 ) / 15)
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

        label.bind("<Button-1>", lambda e, c=card, l=label: on_card_click(c, l, width, height, root))

        label.grid(row=i // 8, column=i % 8, padx=padding_width, pady=padding_height)


    # Run the GUI loop
    root.mainloop()

