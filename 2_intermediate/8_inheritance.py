class Pet:
 def __init__(self, pet_name):
  self.pet_name = pet_name

 def walK(self):
  print(f"could you walk my {self.pet_name} while I am away")



isPet = Pet("pet")
isPet.walK()


class Puppy(Pet):
  def sit(self):
   print("stop barking and sit")


class Kitten(Pet):
 pass


class PetMonkey(Pet):
  def troubling_monkey_pet(self):
   print("This pet is so troubling")


isPuppy = Puppy("puppy")
isPuppy.walK()
isPuppy.sit()

isKitten = Kitten("kitten")
isKitten.walK()

isMonkey = PetMonkey("pet monkey")
isMonkey.troubling_monkey_pet()
isMonkey.walK()

