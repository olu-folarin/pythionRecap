# intro to list comprehension
# the idea behind this is to do carry out an operation on a part or all of a list then add it to the list

cars = ['volvo', 'peugeot', 'aston martin', 'range rover']
nums = [1,4,6,7,3,8]
# below is what it looks like
# new_cars = [car[0].upper() + car[1:] for car in cars]
added_num = [num + num for num in nums]
print(added_num)