class Person:
 def __init__(self, name):
  self.name = name

 def talk(self):
  print("Let's talk hear")
  print(f"I am {self.name} part of TeraAI team of ML engineers")


person = Person("Jax")
print(person.name)
person.talk()

kwera = Person("Kwera")
kwera.talk()

is_name = input("Enter your name: ")
mandu = Person(f"{is_name}")
mandu.talk()