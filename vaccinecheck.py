# user enters an age
# determine if the user is old enough to get a covid vaccine
# determines what kinda vaccine you are eligible for.


age = input('Enter your age: ')

if age:
    age = int(age)
    if age >= 45:
        print('You can get either Moderna, Pfizer, AZ or J&J vaccine')
    elif age >= 16:
        print('You can get every other vaccine except AZ')
    else:
        print('Sorry young fellow, you are not old enough for a jab. Wait till you are 16!')
else:
    print('Are you ageless?')