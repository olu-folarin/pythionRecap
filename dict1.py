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
# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

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

# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])

# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }


# if food in bakery_stock:
#     for v in bakery_stock.values():
#         print(f'Only {v} {food} is left.')
#         break
# else:
#     print(f'{food} : We don\'t make that!')


# # pop, popitems and update
# new_bakery_stock = bakery_stock.copy()
# new_bakery_stock.pop('morning bun')
# new_bakery_stock.popitem()

# food2 = {'yam': 6, 'melon': 7}
# food2.update(new_bakery_stock)
# food2['cookie'] = 5
# food2.pop('toffee cookie')
# print(food2)


# # Data Modeling Exercise: spotify playlist modeling
    # create a list of objects.
    # each list has an author, featured artiste, title, release date and track duration.
    # playlist must be in order

# spotify_playlist = {
#     'artiste': 'Mo\'hits',
#     'album': 'Mo\'hits All Stars',
#     'Year': 2009,
#     'songs': [
#         {'title': 'You bad', 'artiste': ['Wande Coal', 'D\'Banj'], 'duration': 3.5},
#         {'title': 'Suddenly', 'artiste': ['Wande Coal', 'D\'Banj'], 'duration': 4.7},
#         {'title': 'ten ten', 'artiste': ['Wande Coal', 'D\'Banj', 'DrSid', 'Dprince'], 'duration': 4.07}
#     ]
# }

# total_duration = 0
# for song in spotify_playlist['songs']:
#     total_duration += song['duration']
    
# print(total_duration)



# Dictionary Comprehensions
# people = {'elder bro': 'tunde', 'younger bro': 'deola', 'younger sis': 'morenike', 'younger sis': 'jibike', 'youngest sis': 'modupe'}

# # greet = {value + ' hello' for value in people.values()}
# first_cap = {key[0:1].upper() + key[1:]: value[0:1].upper() + value[1:] for key,value in people.items()}
# print(first_cap)



# Exercises
    #1. list one will be the key, while list 2 the value
# list1 = ["CA", "NJ", "RI"]
# list2 = ["California", "New Jersey", "Rhode Island"]
# answer = {list1[i]: list2[i] for i in range(0,3)}
# print(answer)

    