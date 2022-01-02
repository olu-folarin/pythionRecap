# exercise 1
# def product(x,y):
#     return x*y


# exercise 2: day of the week
# def return_day(num_day):
#     days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
#     if num_day > 0 and num_day < len(days):
#         return days[num_day-1]
# print(return_day(3))


# exercise 3: last element
# items = [6,7,8,9]
# def last_element(list_item):
#     if list_item:
#         return list_item[-1]
#     else:
#         return 'Out of range'
# print(last_element(items))


# number compare
def number_compare(x,y):
    if x > y:
        return 'First is greater'
    elif x < y:
        return 'Second is greater'
    else:
        return 'Numbers are equal'
print(number_compare(4.01,4))