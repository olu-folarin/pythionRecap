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
# counts = ''
# for n in range(1,12):
#     counts += '*'
#     print(counts)


# Exercise 2: Stop Copying Me
        # print what is inputed and only stop when when 'stop copying me gets printed'
# converse = input('Pls, what\'s the answer to question 1? ')

# while converse:
#         if converse != 'stop copying me':
#                 print(converse)
#                 converse = input('Pls, what\'s the answer to question 1? ')
#         else:
#                 print('Fine!')

                # OR
# while converse != "stop copying me":
#         converse = input('Pls, what\'s the answer to question 1? ')
# print('Fine, I\'ll stop.')