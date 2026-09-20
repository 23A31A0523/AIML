# DAY 5 - FILE HANDLING


# 1. WRITE MODE - "w"

# file = open("notes.txt", "w")
# file.write("Day 5 - Python File Handling")
# file.close()


# 2. READ MODE - "r"

# file = open("notes.txt", "r")
# content = file.read()
# print(content)
# file.close()


# 3. APPEND MODE - "a"

# with open("notes.txt", "a") as file:
#     file.write("\nLearning append mode")


# 4. READ USING with open()

# with open("notes.txt", "r") as file:
#     print(file.read())


# 5. readline() - reads one line

# with open("notes.txt", "r") as file:
#     line = file.readline()
#     print(line)


# 6. readlines() - reads all lines as a list

# with open("notes.txt", "r") as file:
#     lines = file.readlines()
#     print(lines)


# 7. LOOP THROUGH FILE - PRESENT PRACTICE

# with open("notes.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# 8. FILE HANDLING MINI TASK

with open("student.txt", "w") as file:
    file.write("Name: Kal\n")
    file.write("Branch: CSE\n")
    file.write("Skill: Python\n")

with open("student.txt", "a") as file:
    file.write("Learning: AI/ML")

with open("student.txt", "r") as file:
    print(file.read())