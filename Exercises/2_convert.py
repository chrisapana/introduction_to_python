# comparison operator
# weight converter

myInput = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g : ")

if unit.upper() == "L":
 convertion = myInput * 0.45 
 print(f"You are {convertion} Kilos")
elif unit.upper() == "K" :
 convertion =  myInput / 0.45
 print(f"You are {convertion} pounds ")
