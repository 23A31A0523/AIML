# **Basic Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
floor_div = num1 // num2
remainder = num1 % num2
power = num1 ** num2

print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Division: ", div)
print("Floor Division: ", floor_div)
print("Remainder: ", remainder)
print("Power: ", power)

print("Is first number greater than second?", num1 > num2)
print("Are both numbers equal?", num1 == num2)