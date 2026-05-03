# dictionaries
#  Emoji converter

text = input("> ")
word = text.split(" ")
emoji = {
 ":)": "😁",
 ":(": "😢",
 ":()": "🤔",
}

# print(word)

output = ""
for ch in word:
 output += emoji.get(ch, ch) + " "
print(output)

