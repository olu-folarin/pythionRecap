from random import Random

# save any popped value to a list and while multiplying others by 7 and saving them to another list

# numbers = [1,2,3,4,5,6,7,8,9,10,11]
# popped = []
# by7 = []

# def multipy_by_7(x):
#     for num in x:
#         # print(num)
#         if num % 2 == 0:
#             by7.append(num*7)
#         else:
#             popped.append(num)
#     print(by7)
#     print(popped)
#     # return by7
#     # return popped
# multipy_by_7(numbers)

# coin flip program
# def coin_flip():
#     rand = random()
#     if rand > 0.5:
#         return f'{rand}: head'
#     else:
#         return f'{rand}: tail'
    
# print(coin_flip())


# Exercise 1: Generating even numbers stored in a list

# def generate_evens():
#     even_num = [num for num in range(1,50) if num%2 == 0 and num < 50]
#     return even_num
    
    # or
    # return [x for x in range(1,50) if x%2==0 and x<50]

# print(generate_evens())


# Default parameters: talking animals exercise
animals = ['pig', 'dog', 'duck', 'cat']

def speak(animal = 'dog'):
    for animalia in animals:
        if animalia == 'pig':
            return 'oink'
        elif animalia == 'duck':
            return 'quack'
        elif animalia == 'dog':
            return 'woof'
        elif animalia == 'cat':
            return 'meow'
        else:
            return '?'

print(speak(animals))