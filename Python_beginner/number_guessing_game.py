import random


rand_num = random.randint(1,100)


while True:
    try:
        num = int(input('Guess the number between 1 and 100:'))
        if rand_num < num:
            print('Too high!')
        elif rand_num > num:
            print('Too low!')
        else:
            print("Youre right: ")
            break
    except ValueError: 
        print('please enter right value')

    

   
    