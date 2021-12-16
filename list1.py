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
instructors = []
instructors.extend(['colt', 'blue', 'traversy', 'andrei'])
print(instructors)