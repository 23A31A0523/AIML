# print("--- Python Dictionaries ---")

# student = {
#     "name": "Kal",
#     "branch": "CSE",
#     "cgpa": 8.5,
#     "skill": "Python"
# }

# print(student)
# print("Name:", student["name"])
# print("Branch:", student["branch"])
# print("CGPA:", student["cgpa"])
# print("College:", student.get("college"))
# print("College:", student.get("college", "Not provided"))


# print("\n--- Modifying Dictionary ---")

# student = {
#     "name": "Kal",
#     "branch": "CSE",
#     "cgpa": 8.5,
#     "skill": "Python"
# }

# # Add a new key-value pair
# student["college"] = "Pragati Engineering College"
# print("After adding college:", student)

# # Update existing value
# student["skill"] = "Machine Learning"
# print("After updating skill:", student)

# # Delete a key-value pair
# student.pop("branch")
# print("After removing branch:", student)


# ml_model = {
#     "name": "Random Forest",
#     "accuracy": 91.5
# }

# ml_model["task"] = "Classification"
# ml_model["accuracy"] = 94.2
# ml_model.pop("name")
# print(ml_model)


# print("\n--- Looping Through Dictionary ---")

# model = {
#     "name": "Random Forest",
#     "accuracy": 94.2,
#     "task": "Classification"
# }

# for key, value in model.items():
#     print(key, ":", value)


# scores = {
#     "Python": 90,
#     "SQL": 95,
#     "Machine Learning": 80
# }

# for key,value in scores.items():
#     print(key,"score is",value)


print("\n--- Nested Dictionaries ---")

models = {
    "model1": {
        "name": "Random Forest",
        "accuracy": 94.2
    },
    "model2": {
        "name": "Logistic Regression",
        "accuracy": 91.8
    }
}

print(models)
print("First model:", models["model1"]["name"])
print("First model accuracy:", models["model1"]["accuracy"])
print("Second model:", models["model2"]["name"])

for key, value in models.items():
    print(f"{value['name']} has accuracy {value['accuracy']}")