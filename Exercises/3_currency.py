# comparison operator
# currency convertion

amount = int(input("how much do you have: "))
newCurrency = input("(D)US or (C)Gh : ")

if newCurrency == "$":
 convert = amount * 11
 print(f"You have {convert} USD")
elif newCurrency.upper() == "C":
 convert = amount / 11
 print(f"You have {convert} Gh cedis") 