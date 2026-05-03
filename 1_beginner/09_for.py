# for loops

for value in "Django":
 print(value)

for isValue in ["hash", "tree", "array"]:
 print(isValue)


for num in [1, 5, 8, 6, 7, 2]:
 print(num)

for position in ["CEO", "CTO", "Acountant", "frontend dev", "backend dev", "Network eng", "DevSec"]:
 print(position)


for num2 in range(6):
 print(num2)
 

for item in ["monitor", "desk", "stand"]:
 print(item)


for isNum in range(4, 10):
 print(isNum)

print("step in range funtion")
# step in range funtion
for newNum in range(2, 10, 3):
 print(newNum)


# total prices
prices = [15, 12, 299, 845, 499]
total = 0 

for newValue in prices:
 # total = total + newValue
 total += newValue
print(f"Total: ${total}")



