
# Strings

msg = """
Hey Peter,

Do you want to try
 
Haha!
"""  
print(msg)

message = '''
Hi there,

Your message has been recieved and will be delivered shortly.

thanks,
support team

'''
print(message)

push = "let's get back on track"
print(push[0])
print(push[4])
print(push[5])
print(push[-1])
print(push[-2])
print(push[0:7])
print(push[-5:-1])
print(push[:-1])
print(push[:8])
print(push[3:])
print(push[:])
print(push[1:-1])



# Formatted strings
newValue = "Jack"
new_Value = "Rag"

# Jack [Rag] is a pythonista

newMessage = newValue + ' [' + new_Value + '] is a pythonista'
print(newMessage)

new_Message = f'{newValue} [{new_Value}] is a pythonista'
print(new_Message)




# String Methods
isMessage = "Python is easy"
# general purpose functions
# print & len
print(len(isMessage))

# string methods

print(isMessage.upper())
print(isMessage.lower())
print(isMessage.title())

# case sensitive
# find method for string index
print(isMessage.find("s"))  
print(isMessage.find('z'))
print(isMessage.find('easy'))
print(isMessage.replace('easy', 'necessary'))
print(isMessage.replace('Easy', 'necessary'))
# in operator for the boolean value
# "..." in sting_variable
print('Python' in isMessage)
print('Easy' in isMessage)
