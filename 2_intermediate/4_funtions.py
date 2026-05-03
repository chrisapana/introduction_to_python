def network_with_attendees():
 print("Hello there")
 print("Nice meeting you here")
 print("What are you recent projects")

 
print("Begin")
network_with_attendees()
print("End")


# parameters - placeholder in our funtion
# arguments - actual information in the funtion

def invite_expect(name):
 # name = "Jack"
 print(f"Hello {name}")
 print("""we represent Moon company 
Would you like to visit our stand
checkout our new AI models""")

invite_expect("Ben")


def say_hello(friend, role):
 print(f"Hello {friend} {role}!")
 print(f"Welcome to the team")


say_hello("Rookie", "Junior Dev")


# keyword argument -- only to be added after a positional argument 
def calc_cost(shipping, discount, total):
 print(f"You'll need about {shipping} for shipping\n and discount at {discount} to make a total of {total} USD ")
 print("Are you insisting on this model")


calc_cost(shipping=300, discount=200, total=1499)

calc_cost(10, 20, total=299)
calc_cost(30, discount=50, total=49)

# return statement
def exponent(is_num):
 print(is_num * is_num)

result = exponent(7)
print(result)

print(exponent(12))

# return -- the value/object "none" from the funtion execution is removed 
def square(num):
 return num * num

outcome = square(4)
print(outcome)

print(square(14))

