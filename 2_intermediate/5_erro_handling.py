try:
 cost = int(input("enter value: "))
 print(cost)
except ValueError:
 print("Invalid value")



try:
 age = int(input("Age: "))
 income = 7000
 risk = income / age
 print(age)
 print(risk)
 print(f"Can you take the risk of {risk} % ")
except ZeroDivisionError:
 print("Income must be more than 0")
except ValueError:
 print("Invalid value")


