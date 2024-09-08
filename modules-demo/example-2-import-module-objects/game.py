# game.py
# import only the draw_new_game module
from draw import draw_new_game

def play_game():
    print('play_game function called')

def main():
    play_game()
    draw_new_game() # this is a function we imported   

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()