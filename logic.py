import screen
import data

def run_game(root, screen_width, screen_height, base_color, mainframe):
    basic_explanation="HI! this is the pokemon memory card game!\nYou can press the cards facing down to see what is underneath.\n If both cards are the same they will stay facing up\nOtherwise they will go back to facing down\n\nwin by finding all the pairs!"
    screen.message_to_user(basic_explanation)


    screen.activate_screen(root, screen_width, screen_height, base_color, mainframe)





