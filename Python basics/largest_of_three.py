# **Prob1: Largest of 3 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print("Largest number: ",num1)
elif num2>num3:
    print("Largest number: ",num2)
else:
    print("Largest number: ",num3)