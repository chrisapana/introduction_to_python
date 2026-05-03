
import random


class Dice:
 def roll(self):
  first = random.randint(1, 6)
  second = random.randint(1, 6)
  # return (first, second)
  return first, second


# returning tuple from funtion don't need parenthesis

dice = Dice()
print(dice.roll())
