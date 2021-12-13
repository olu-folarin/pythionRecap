from random import choice

# city = input('name of your city is? ')

# if city == 'ikorodu' or city == 'epe':
#     print('you live in lagos')
# elif city == '' or city == 'lagos':
#     print('you must live somewhere in lagos')
# else:
#     print('you don\'t live in lagos')

food  = choice(['rice', 'beans', 'eba', 'salad', 'amala', 'efo riro'])

# if food == 'rice' or food == 'eba':
#     print(f'{food}: carbohydrate')
# elif food == 'beans':
#     print(f'{food}: protein')
# elif food == 'salad':
#     print(f'{food}: fruits')
# elif food == 'amala':
#     print(f'{food}: yoruba')
# elif food == 'efo riro':
#     print(f'{food}: soup')
# else:
#     print('what do you eat?')

if not ((food == 'rice') or food == 'eba'):
    print(f'{food}: It\'s either protein, fruits, yoruba or soup')
else:
    print(f'{food} is a type of carbohydrate')