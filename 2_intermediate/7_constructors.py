class Point:
 def __init__(self, x, y):
  self.x = x
  self.y = y
 def move(self):
  print("move")

 def draw(self):
  print("draw")


isPoint = Point(3, 45)
# isPoint.x = 3
isPoint.move()
print(isPoint.x)
isPoint.draw()
print(isPoint.x, isPoint.y)

# updated
isPoint.x = 98
print(isPoint.x)
