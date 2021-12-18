import random

random_num = random.randint(1,10)
# equate guess to None so you don't make comparison with something that does not exist
# guess = None

# while guess != random_num:
#     guess = input('Pick a num fro 1 to 10: ')
#     guess = int(guess)
#     if guess < random_num:
#         print('Too low!')
#     elif guess > random_num:
#         print('Too high!')
#     else:
#         print('You won!')
        
#     print(guess)

while True:
    guess = input('Pick a num fro 1 to 10: ')
    guess = int(guess)
    if guess < random_num:
        print('Too low!')
    elif guess > random_num:
        print('Too high!')
    else:
        print('You win!')
        replay = input('Want to play again? (y/n) ')
        if replay == 'y':
            random_num = random.randint(1,10)
            guess = None
        else:
            print('Thanks for playing.')
            break