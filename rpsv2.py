from random import randint


# proper AI
player = input('Is it rock, paper or scissors? ')
comp = ['rock', 'paper', 'scissors'][randint(0,2)]
player = player.lower()


if player:
    if player == comp:
        print(f'Player {player} - Comp {comp}--> Deuce')
    elif player == 'rock':
        if comp == 'scissors':
            print(f'Player {player} - Comp {comp}--> player wins!')
        elif comp == 'paper':
            print(f'Player {player} - Comp {comp}--> comp wins!')
    elif player == 'paper':
        if comp == 'rock':
            print(f'Player {player} - Comp {comp}--> player wins')
        elif comp == 'scissors':
            print(f'Player {player} - Comp {comp}--> comp wins!')
    elif player == 'scissors':
        if comp == 'paper':
            print(f'Player {player} - Comp {comp}--> player wins!')
        elif comp == 'rock':
            print(f'Player {player} - Comp {comp}--> comp wins!')
    else:
        print('What\'s the catch?')