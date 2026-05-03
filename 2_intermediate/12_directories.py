from pathlib import Path

"""
path = Path("exercises")
print(path.exists())

path1 = Path("emails")
path2 = Path("clients")
# print(path1.exists())
# print(path2.exists())


# print(path1.mkdir())
# print(path2.mkdir())


# print(path1.rmdir())
# print(path2.rmdir())


"""


new_path = Path()
# print(new_path.glob("*"))
# print(new_path.glob("*.*"))
# print(new_path.glob("*.xls"))
# print(new_path.glob("*.py"))

for file in new_path.glob("*"):
 print(file)


