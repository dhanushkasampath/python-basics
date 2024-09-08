# game.py
# import the draw module
from draw import *

def play_game():
    print('play_game function called')

def main():
    play_game()
    # we were able to import all below objects
    draw_game()
    draw_new_game()  

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()