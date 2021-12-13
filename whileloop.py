# fav_food = input('What\'s your favorite food? ')

# while fav_food !='beans':
#     print('Incorrect!')
#     fav_food = input('What\'s your favorite food? ')
# print('On point!')

# num = 1

# while num < 11:
#     print(num)
#     num += 1


# Exercise 1
# print the emoji ('\U0001f600') using a for loop and a while loop from 1 to 10 in a leftt-angle triangular shape.

        # with a while loop
# counts = 1
# emoji = ''
# while counts < 11:
#     print(emoji)
#     counts += 1
#     emoji += '*'
        # OR
# counts = 1

# while counts < 12:
#     print('*' * counts)
#     counts += 1

        # with a for loop
# pyramid = ''

# for num in range(1,11):
#     if num < 11:
#         pyramid += '*'
#         print(pyramid)
#     else:
#         print('the end!')
# print(pyramid)

        # OR: :(
counts = ''
for n in range(1,12):
    counts += '*'
    print(counts)