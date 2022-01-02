# exercise 1
# def product(x,y):
#     return x*y


# exercise 2: day of the week
def return_day(num_day):
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    if num_day > 0 and num_day < len(days):
        return days[num_day-1]
print(return_day(3))