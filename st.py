# Tuples

# letters = ('a', 'b', 'c', 'd')
# locations = {
#     (23, 45): 'London',
#     (43, 87.4): 'Tokyo',
#     (34, 52): 'Berlin'
# }
# print(locations.keys())

# days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

# r = len(days) - 1
# while r >= 0:
#     print(days[r])
#     r -= 1

# nums = (1,2,5,6,3,6,8,2,4,5)
# for num in nums:
#     if nums.count(num) > 1:
#         print(f'{num} occured {nums.count(num)} times.')
#     else:
#         print(f'{num} No more than once.')


# Set

states = {'abia', 'adamawa', 'akwa ibom', 'kogi', 'kano', 'kaduna', 'edo'}
# states.add('lagos')
# states.remove('abia')
# states.discard('adamawa')
# copied_states = states.copy()

# math set
other_states = {'bayelsa', 'kebbi', 'oyo', 'osun', 'ekiti', 'edo'}
# combined = states | other_states
intersect = states & other_states
print(intersect)