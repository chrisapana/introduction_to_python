num1 = 10
num2 = 7
num01 = num1 / num2
num02 = num1 * num2
num03 = num1 + num2
num04 = num1 - num2

print(num01)
print(num02)
print(num03)
print(num04)

# integer --- //
num05 = num1 // num2
print(num05)


# modulus --- %
num06 = num1 % num2
print(num06)



# exponent --- **
num07 = num1 ** num2
print(num07)

# others
num08 = num07 + 6
print(num08)

num07 += 9
print(num07)

num07 -= 2
print(num07)

num07 /= 7 
print(num07)

num07 *= 7 
print(num07)

# Operator precedence
# 1 -- parenthesis
# 2 -- exponentiation
# 3 -- multiplication or division  
# 4 -- addition or subtraction

x_num = 8 + 6 * 3
print(x_num)

y_num = 8 + 6 * 3 ** 2
print(y_num)

z_num = (8 + 6) * 3 ** 2
print(z_num)




# Math functions 

isNum = 12.87

print(round(isNum))
print(abs(isNum))
print(abs(-896))

# inbuilt_math module 
import math

print(math.ceil(isNum))
print(math.ceil(12.001))

print(math.floor(isNum))
print(math.floor(12.001))
