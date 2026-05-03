#  modules && function

"""
numbers = [8, 3, 6, 18, 24, 2, 9]
max = numbers[0]
for num in numbers:
 if num > max:
  max = num
print(max)
"""


def find_max(numbers):
 is_max = numbers[0]
 for num in numbers:
  if num > is_max:
   is_max = num
 return is_max


"""
numbers = [8, 3, 6, 18, 24, 2, 9]
# print(find_max(numbers))

newMax = find_max(numbers)
print(newMax)
"""

