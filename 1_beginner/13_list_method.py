numbers = [45, 76, 23, 97, 89, 12]
print(numbers)

# add at end
numbers.append(100)
print(numbers)

numbers.insert(5, 3)
print(numbers)

numbers.remove(23)
print(numbers)

# numbers.clear()
# print(numbers)

# remove last object
numbers.pop()
print(numbers)

# the exitence of an object
print(numbers.index(97))
# exitence
print(89 in numbers)
print(44 in numbers)


# count occurances of an object
print(numbers)
numbers.insert(2, 45)
print(numbers)
print(numbers.count(45))

numbers.append(45)
print(numbers)
# count
print(numbers.count(45))

# sort objects
print(numbers.sort())
# sort
numbers.sort()
print(numbers)

# reverse
numbers.reverse()
print(numbers)

# copy
numbers2 = numbers.copy()
numbers.append(100)
print(numbers)
print(numbers2)


# remove duplicates
isNum = [3, 5, 6, 5, 2, 1, 7, 3, 3, 6]
fine = []
for num in isNum:
 if num not in fine:
  fine.append(num)
print(fine)

isNum.sort()
print(isNum)
fine.sort()
print(fine)