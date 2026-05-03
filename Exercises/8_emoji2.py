# funtions
#  Emoji converter

def emoji_convert(text):
 word = text.split(" ")
 emoji = {
  ":)": "😁",
  ":(": "😢",
  ":()": "🤔",
 }
 output = ""
 for ch in word:
  output += emoji.get(ch, ch) + " "
 return output


text = input("> ")
print(emoji_convert(text))

