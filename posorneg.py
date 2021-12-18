from random import randint

x = randint(-20, 30)
y = randint(-20, 30)


if x > 0 and y > 0:
    print(f'{x}, {y}: x and y are positives.')
elif x < 0 and y < 0:
    print(f'{x}, {y}: x and y are negatives.')
elif x > 0 or y < 0:
    print(f'{x}, {y}: x is positive and y is negative.')
else:
    print(f'{x}, {y}: x is negative and y is positive.')