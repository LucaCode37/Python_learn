import random

a = ['r','p','s']


def get_user_choice():
    while True:
        input_user = input('Rock, Paper, Scissors? (r/p/s)').lower()
        if input_user in a:
            return input_user
        else:
            print('Mistake try again')
            continue


def display(input_user,rand_input):
    print(f'You chose {input_user}')
    print(f'Computer chose {rand_input}')


def determine_winner(input_user, rand_input):
    if input_user == rand_input:
        print('Tie!')
    elif (input_user == 'r' and rand_input == 's')\
        or (input_user == 'p' and rand_input == 'r')\
        or (input_user == 's' and rand_input == 'p'):
        print('You win')
    else: print ('You Loose')


def play_game():
    while True:
        input_user = get_user_choice()
    
        rand_input = random.choice(a)

        display(input_user, rand_input)

        determine_winner(input_user, rand_input)

        input_keepgoing = input('Keep going? (y/n)').lower()
        if input_keepgoing != 'y': break
    

play_game()
    




