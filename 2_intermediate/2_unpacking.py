# unpacking can be used in tuples or lists

items = (2, 3, 5, 7)
mul = items[0] * items[0] * items[0] * items[0]
# x = items[0]
# y = items[1]
# z = items[2]
# r = items[3]
x, y, z, r = items

mul2 = x * y * z * r

print(x)
print(y)
print(z)
print(r)


