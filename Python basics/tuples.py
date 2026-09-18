# print("--- Python Tuples ---")

# ml_tools = ("NumPy", "Pandas", "Scikit-learn", "Matplotlib")
# print("Tuple:", ml_tools)
# print("First tool:", ml_tools[0])
# print("Last tool:", ml_tools[-1])
# # Slicing
# print("First two:", ml_tools[:2])
# # Length
# print("Number of tools:", len(ml_tools))


# print("\n--- Tuple Unpacking ---")

# student = ("Kal", "CSE", 8.5)
# name, branch, cgpa = student
# print("Name:", name)
# print("Branch:", branch)
# print("CGPA:", cgpa)


model_info = ("Random Forest", 95.2, "Classification")
model, accuracy, task = model_info
print("Model: ",model)
print("Accuracy: ",accuracy)
print("Task: ",task)


scores = (85, 90, 92, 88, 90)
print(len(scores))
print(max(scores))
print(min(scores))
print(scores.count(90))