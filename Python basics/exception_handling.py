# 1. try + except with specific exceptions

# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("Please enter a valid number")
# except ZeroDivisionError:
#     print("Cannot divide by zero")


# 2. try + except + else + finally - PRESENT PRACTICE

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result:", result)
finally:
    print("Program execution completed")