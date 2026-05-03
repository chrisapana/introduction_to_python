# lists
# remove duplicates

isNum = [3, 5, 6, 5, 2, 1, 7, 3, 3, 6]
fine = []
for num in isNum:
 if num not in fine:
  fine.append(num)
print(fine)
