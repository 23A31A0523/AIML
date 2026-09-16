# **Student Grade Calculator
marks = int(input("Enter marks: "))
if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
elif 60 <= marks < 70:
    print("Grade D")
elif 0 <= marks < 60:
    print("Fail")
else:
    print("Invalid marks")