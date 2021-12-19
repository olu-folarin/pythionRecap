# intro to list comprehension
# the idea behind this is to do carry out an operation on a part or all of a list then add it to the list

cars = ['volvo', 'peugeot', 'aston martin', 'range rover']
nums = [1,4,6,7,3,8]
# below is what it looks like
# new_cars = [car[0].upper() + car[1:] for car in cars]
# added_num = [num + num for num in nums]
# print(added_num)




# list comprehension with conditional logic
# add_num = [num + num for num in nums]
# print(add_num)

# list comp with an if statement
# even = [num for num in nums if num % 2 == 0]
# start_with_v = [car for car in cars if car[0] != 'v']


# list comp with double logical statements
# odd = [num+num if num % 2 != 0 else 0 for num in nums]
even = [num * 10 if num % 2 == 0 else 'odd' for num in nums]
print(even)