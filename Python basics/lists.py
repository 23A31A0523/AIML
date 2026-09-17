# skills = ["Python", "SQL", "Machine Learning", "Git"]
# print(skills)
# print(skills[0])
# print(skills[2])

# print("\n--- Accessing List Items ---")

# skills = ["Python", "SQL", "Machine Learning", "Git"]
# print(skills[0])  
# print(skills[1])  
# print(skills[-1]) 
# print(skills[-2])  


# print("\n--- Modifying Lists ---")

# skills = ["Python", "SQL", "Machine Learning", "Git"]
# # Change an existing item
# skills[3] = "GitHub"
# print("After change:", skills)

# # Add item at the end
# skills.append("NumPy")
# print("After append:", skills)

# # Add item at a specific position
# skills.insert(2, "Pandas")
# print("After insert:", skills)

# # Remove item by value
# skills.remove("SQL")
# print("After remove:", skills)

# # Remove the last item
# removed_skill = skills.pop()
# print("Removed:", removed_skill)
# print("Final list:", skills)


print("\n--- List Slicing ---")

scores = [72, 85, 91, 68, 95, 88, 76]
print("All scores:", scores)
print("First 3:", scores[0:3])
print("From index 2:", scores[2:])
print("Up to index 4:", scores[:4])
print("Last 3:", scores[-3:])
print("Every second item:", scores[::2])
print("Reversed:", scores[::-1])

