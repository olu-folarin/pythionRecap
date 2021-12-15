from random import randint

# keep track of the scores
gamer_wins = 0
comp_wins = 0
winning_score = 4

while gamer_wins < winning_score and comp_wins < winning_score:
    print(f'Gamer Score: {gamer_wins} Computer Score: {comp_wins}')
    print('<<< rock >>>')
    print('<<< paper >>>')
    print('<<< scissors >>>')

    gamer = input('(Make a pick): ').lower()
    # give the player the chance to quit
    if gamer == 'quit' or gamer == 'q':
        break
    random_num = randint(1, 3)

    if random_num == 0:
        comp = 'rock'
    elif random_num == 1:
        comp = 'paper'
    else:
        comp = 'scissors'

    print(f'The computer played {comp}')

    if gamer == comp:
        print('It\'s a tie!')
    elif gamer == 'rock':
        if comp == 'paper':
            print('You lose!')
            comp_wins += 1
        else:
            print('You win :)')
            gamer_wins += 1
    elif gamer == 'paper':
        if comp == 'rock':
            print('You win :)')
            gamer_wins += 1
        else:
            print('You lose!')
            comp_wins += 1
    elif gamer == 'scissors':
        if comp == 'rock':
            print('You lose!')
            comp_wins += 1
        else:
            print('You win :)')
            gamer_wins += 1
    else:
        print('Pls enter a valid move.')

# print a message to show who wins or loses
if gamer_wins > comp_wins:
    print('Congratulations, you win!')
elif gamer_wins == comp_wins:
    print('It\'s a tie! Better luck next time.')
else:
    print('Sorry, you lose!')

# print the winner
print(f'Final Scores--> Gamer: {gamer_wins} Computer: {comp_wins}')
