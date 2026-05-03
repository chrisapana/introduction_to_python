# while loops

secretNum = 4
guessCount = 0
guessLimit = 3

while guessCount < guessLimit:
 guess = int(input("what is your guess: "))
 guessCount += 1
 if guess == secretNum:
  print("You've won!")
  break
else:
 print("Oops")