# dictionaries
# spell -- put contact info into words

info = input("what is your number: ")

digit_bank = {
 "0": "zero",
 "1": "one",
 "2": "two",
 "3": "three",
 "4": "four",
 "5": "five",
 "6": "six",
 "7": "seven",
 "8": "eight",
 "9": "night",
}

output= ""
for char in info:
 output += digit_bank.get(char, "!") + " "
print(output)

