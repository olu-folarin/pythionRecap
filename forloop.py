# for num in range(1,9):
#     if num%2 == 0:
#         print(f'{num} is an even number.')
#     else:
#         print(f'{num} is an odd number.')


# RANGE
# for num in range(25,-1,-1):
#     print(num)


# Exercise 1
    # add up every odd number from 10 to 20
    # store the total value in a variable
# tots = 0

# for num in range(10,21):
#     if num%2 != 0:
#         tots += num
#     else:
#         print('even')
    
# print(tots)


# Exercise 2
    # enter an integer then print something the number of integer entered: this was an interesting exercise
# times = input('How many times do you have? ')
# times = int(times)

# for time in range(times):
#         print('Show me your fingers!')


# Exercise 3
# loop through 1-20 (inclusive)
    # for 4 and 13, print 'the number is unlucky'
    # for even numbers, 'x is even'
    # for odd numbers, 'x is odd'
    
# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f'{num} is unlucky.')
#     elif num % 2 == 0:
#         print(f'{num} is even.')
#     else:
#         print(f'{num} is odd.')

            # OR

for num in range(1,21):
    if num == 4 or num == 13:
        status = 'unlucky'
    elif num % 2 == 0:
        status = 'even'
    else:
        status = 'odd'
    print(f'{num} is {status}.')