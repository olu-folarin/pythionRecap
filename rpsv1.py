# a rock, paper, scissors game
# rock > scissors, rock < paper, scissors > paper, paper > rock

print('choose: Rock, Paper or Scissors')

p1 = input('Player1, make a move! ')
p2 = input('Player2, make a move! ')


if p1 and p2:
    if p1 == p2:
        print('Draw')
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            print('P1 wins!')
        elif p2 == 'Paper':
            print('P2 wins!')
    elif p1 == 'Paper':
        if p2 == 'Scissors':
            print('P1 wins!')
        elif p2 == 'Paper':
            print('P2 wins!')
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            print('P1 wins!')
        elif p2 == 'Rock':
            print('P2 wins!')
    else:
        print('Which player are you?')
elif not p1 and p2:
    print('Rock, Paper or Scissors')
else:
    print('Enter something appropriate!')