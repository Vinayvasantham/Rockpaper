import random


def play():
    # choice = input('You want to play Rock paper and sciccor game (y/n):')
    choice = 'y'
    while choice != 'n':
        user  = input("what's your chioice rock[r] , paper[p] or scissor[s]:")
        computer = random.choice(['r','p','s'])

        if user == computer:
            print('Tie')

        elif iswin(user,computer):
            print('YOU WIN\n')
        else:
            print('Computer win\n')
        choice = input('You want to play Rock paper and sciccor game (y/n):')

    print('Thanks for playing game.. See you again!')



def iswin(player,opponent):
    if (player =='r' and opponent == 'p' or player == 's' and opponent == 'p' or player == 'r' and opponent == 's'):
        return True


play()