import os
import random
from PIL import Image, ImageTk  

image_folder = "images/front_images"
image_files = os.listdir(image_folder)

#move to sepeare file
class cardPokemon:
    def __init__(self, id, image_front, image_back = "images/pokemon_card_backside.png", orientation = "face_down"):
            self.id = id
            self.image_front = image_front
            self.image_back = image_back
            self.orientation = orientation

    def change_orientation(self):
        if self.orientation == "face_up":
            self.orientation = "face_down" 
        else:
            self.orientation = "face_up"
    

cardDeck = []

def randomize_deck(cardDeck):
    random.shuffle(cardDeck)

for index, filename in enumerate (image_files):        
        image_path = os.path.join(image_folder , filename)
        cardDeck.append (cardPokemon(index + 1, image_path))
randomize_deck(cardDeck)



def fixed_pokemon_deck(cardDeck, height, width):
    number_cards = height * width / 2
    number_cards = int(number_cards)
    cardDeck = cardDeck[0:number_cards]
    cardDeck = cardDeck * 2
    randomize_deck(cardDeck)
    return cardDeck

     
