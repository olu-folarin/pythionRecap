from random import choice

# friends = [
#     {'name': 'Kola', 'age': 32, 'gender': 'male', 'occupation': 'Accountant', 'location': 'UK'},
#     {'name': 'Ik', 'age': 32, 'gender': 'male', 'occupation': 'DevOps Engineer', 'location': 'USA'}, 
#     {'name': 'Tope', 'age': 31, 'gender': 'male', 'occupation': 'Banker', 'location': 'NGR'},
#     {'name': 'Damola', 'age': 30, 'gender': 'female', 'occupation': 'Banker', 'location': 'NGR'},
#     {'name': 'Sesede', 'age': 25, 'gender': 'female', 'occupation': 'Fashion Designer', 'location': 'NGR'}
#     ]

# friend = {'name': 'kyle xy', 'age': 43, 'height': 5.8}
# for loop

    # this will print the value
# for val in friend.values():
#     print(val)
    
    # this will print the key
# for key in friend.keys():
#     print(key)
    
    # this will print the key and value
# for key,val in friend.items():
#     print(key,val)

# Exercise 1: add donations to total_donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

# total_donations = 0
# for v in donations.values():
#     total_donations += v

# isThere = 'sam' in donations
# isValue = 13.0 in donations.values()
# print(isValue)


# dict methods
# donations1 = donations.copy()
# print(donations1)

# user_profile = {}.fromkeys(['name', 'age', 'gender', 'occupation'], 'unavailable')

# # using get
# print(donations.get('stan'))

# Exercise 2
    # if food is an item in bakery_stock, print out a string showing how much of it is left, if not, print 'We don't that!'

food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


# if food in bakery_stock:
#     for v in bakery_stock.values():
#         print(f'Only {v} {food} is left.')
#         break
# else:
#     print(f'{food} : We don\'t make that!')


# # pop, popitems and update
new_bakery_stock = bakery_stock.copy()
new_bakery_stock.pop('morning bun')
print(new_bakery_stock)