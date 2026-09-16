# **Simple Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "python123":
        print("Login successful!")
    else:
        print("Wrong password.")
else:
    print("User not found.")