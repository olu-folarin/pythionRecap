import random

AI = random.randint(1,11)
guess = input('Guess a number: ')
guess = int(guess)
nan = str(guess)

while input:
    if guess == AI:
        print(f'AI{AI}:You{guess}: You win!')
        replay = input('Do you wish to replay? ')
        if replay == 'y':
            AI = random.randint(1,11)
            guess = input('Guess a number: ')
        elif replay == 'n':
            print('Thanks for playing!')
            break
        else:
            print('y for yes or n for no')
            AI = random.randint(1,11)
            guess = input('Guess a number: ')
    else:
        print(f'AI{AI} : You{guess}: You lose!')
        replay = input('Do you wish to replay? ')
        if replay == 'y':
            AI = random.randint(1,11)
            guess = input('Guess a number: ')
        elif replay == 'n':
            print('Thanks for playing!')
            break
        else:
            print('y for yes or n for no')