import os

image_folder = "images/front_images"
image_files = os.listdir(image_folder)

class cardPokemon:
        def __init__(self, id, image_front, image_back = "images/pokemon_card_backside.png", orientation = "up"):
                self.id = id
                self.image_front = image_front
                self.image_back = image_back
                self.orientation = orientation

cardDeck = []
for index, filename in enumerate (image_files):        
        image_path = os.path.join(image_folder , filename)
        cardDeck.append (cardPokemon(index + 1, image_path))


