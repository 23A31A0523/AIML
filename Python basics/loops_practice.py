# skills = ["Python", "SQL", "Machine Learning", "Git"]
# for skill in skills:
#     print(f"I am learning {skill}")


# scores = [78, 92, 65, 88, 95]
# for score in scores:
#     if score >= 90:
#         print(f"{score} - Excellent")
#     elif score >= 75:
#         print(f"{score} - Good")
#     else:
#         print(f"{score} - Needs Improvement")


# accuracies = [82, 91, 76, 95, 88]
# for acc in accuracies:
#     if acc >= 90:
#         print(f"{acc} - High accuracy")
#     elif 80 <= acc < 90:
#             print(f"{acc} - Good accuracy")
#     else:
#             print(f"{acc} - Low accuracy")


# **while loop
print("\n--- While Loop ---")

count = 1

while count <= 5:
    print("Iteration:", count)
    count += 1


# **break
print("\n--- Break ---")

for number in range(1, 10):
    if number == 5:
        break
    print(number)


# **continue
print("\n--- Continue ---")

for number in range(1, 6):
    if number == 3:
        continue
    print(number)