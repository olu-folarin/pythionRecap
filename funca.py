# save any popped value to a list and while multiplying others by 7 and saving them to another list

numbers = [1,2,3,4,5,6,7,8,9,10,11]
popped = []
by7 = []

def multipy_by_7(x):
    for num in x:
        # print(num)
        if num % 2 == 0:
            by7.append(num*7)
        else:
            popped.append(num)
    print(by7)
    print(popped)
    # return by7
    # return popped
multipy_by_7(numbers)