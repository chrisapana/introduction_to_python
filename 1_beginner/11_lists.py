# lists

build = ["mat", "steel", "cement", "wood"]
print(build)

for x in build:
 print(x)


print(build[0:1])
print(build[0:2])
print(build[2:])
print(build[2])
print(build[-2])
print(build[0])
print(build[:3])
print(build[:])

build[0] = "tiles"
print(build)


is_Num = [89, 67, 2, 76, 98, 34, 25]
max = is_Num[0]
for num in is_Num:
 if num > max:
  max = num
print(max)