import random

while True:
    des = input("Y/N?").lower()

    if des == 'y':
        first_dice = random.randint(1,6)
        secound_dice = random.randint(1,6)
        print(f'({first_dice},{secound_dice})')
    elif des == 'n':
        print('Thanks for Playing')
        break
    else:
        print('Invalud choise')





