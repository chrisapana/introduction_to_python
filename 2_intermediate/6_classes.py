class Point:
 def move(self):
  print("move")

 def draw(self):
  print("draw")


isPoint = Point()
isPoint.move()

isPoint.x = 23
isPoint.y = 67

print(isPoint.x)
print(isPoint.y)
isPoint.draw()


newPoint = Point()

newPoint.x = 899

print(newPoint.x)
# print(newPoint.draw())
# print(newPoint.move())
newPoint.move()



