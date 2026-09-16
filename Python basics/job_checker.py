#Job checker
cgpa = float(input("Enter your cgpa: "))
backlogs = input("Do you have active backlogs? (Yes/No) ")
python = input("Do you know python? (Yes/No) ")

if cgpa >= 7:
    if backlogs == "No":
        if python == "Yes":
            print("Eligible for the role.")
        else:
            print("Not eligible for the role.")
    else:
        print("Not eligible for the role.")
else:
    print("Not eligible for the role.") 