import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissor\n")
    computer = random.choice(['r', 'p', 's'])# let the computer to select one out of these 3

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r   logic to win
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # returns true if player wins
    if(player == 'r' and opponent == 's') \
    or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'):
        return True

print(play())        