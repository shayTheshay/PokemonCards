from logic import run_game
from window_config import init_window


def main():
    #CR: call the init window from window configure file
    root, screen_width, screen_height, base_color, mainframe =  init_window()
    
    run_game(root, screen_width, screen_height, base_color, mainframe)

if __name__ == "__main__":
    main()