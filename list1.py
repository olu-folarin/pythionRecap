# item = input('Add an item to your cart: ').lower()
# stored_items = []

# while item:
#     stored_items.append(item)
#     if len(stored_items) < 7:
#         item = input('ENter an item to add to your cart: ')
#     else:
#         print('Goodbye!')
#         break

# print(stored_items)

# food = ['rice', 'beans', 'garri', 'spaghetti', 'plantain']
# index = 0

# while index < len(food):
#     print(f'{index +1}: {food[index]}')
#     index += 1


# Exercise 1
# combine all the items in a list to form a long, meaningless string saved to a variable
# jombo = ['melon', 'cat', 'yeast', 'thyroid', 'wiki', 'nasa', 'lassa']
# mombo = ''

# for word in jombo:
#     mombo += word.upper()
# print(mombo)


# METHODS
# car_names = ['tesla', 'toyota', 'cardilac', 'ford', 'rivian']

# .append() only takes one argument (int, str, list)
# car_names.append(['poleone', 'hyundai'])

# extend only takes an argument, a list with one or more values.
# car_names.extend(['jaguar'])

# car_names.insert(1, 'porsche')
# print(car_names)


# Exercise 2: add items to an empty list
# instructors = []
# instructors.extend(['colt', 'blue', 'traversy', 'andrei'])
# print(instructors)


# Methods: clear, remove and pop
fruits = ['papaya', 'lemon', 'apple', 'orange', 'lemon','melon', 'peer']

# check_fruit = input('See if this fruit is in the database: ').lower()


#   This still needs to be worked on
# for fruit in fruits:
#     if check_fruit:
#         if check_fruit == fruit:
#             print(f'We have {check_fruit}')
#             break
#         else:
#             print(f'We don\'t have {check_fruit}, but we have {fruit}')
#     else:
#         print('You entered nothing!')

# fruit = fruits.pop(-1)
# fruits.clear()
# fruits.remove('lemon')
# print(fruits)


# Methods: reverse, sort, index, count
# fruits.reverse()
# fruit_count = fruits.count('lemon')
# indexed_fruit = fruits.index('peer', 3, 7)
# new_fruits = ' '.join(fruits)
# print(new_fruits)


# slice: doesn't require a dot-separated value unlike other methods
    # when a negative counter is used, the number line gets flipped.

# slice_two = fruits[::2]
# print(slice_two)
# backwards_by2 = fruits[::-2]
# flipped_numberline = fruits[5:3:-1]
sliced_string = fruits[3][::-1]
print(sliced_string)