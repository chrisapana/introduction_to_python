# Nested loops

for x in range(4):
 for y in range(3):
  print(f"({x}, {y})")

# for x in range(4):
#  for y in range(3):
#   print(x, y)


for nest in [4, 7, 2, 5, 1]:
 for nex in ["x"]:
  print(nest * nex)

numbers = [0, 1, 2, 3, 4]
for y_count in numbers:
 print("y" * y_count)

num3 = [8, 6, 4, 2]
for x_count in num3:
 output = ""
 for count in range(x_count):
  output += "x"
 print(output)
