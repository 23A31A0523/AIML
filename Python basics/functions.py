# def greet():
#     print("Welcome to AI/ML!")
# greet()


# def greet_user(name):
#     print(f"Hello {name}, welcome to AI/ML!")
# greet_user("Kal")


# def check_accuracy(acc):
#     if acc >= 90:
#         print("High accuracy")
#     elif acc >= 80:
#         print("Good accuracy")
#     else:
#         print("Low accuracy")
# check_accuracy(92)
# check_accuracy(85)
# check_accuracy(74)


# def calculate_average(s1,s2,s3):
#     avg = (s1 + s2 + s3) / 3
#     return avg
# average = calculate_average(80,90,100)
# print(average)


#default parameter
# def greet(name="Student"):
#     print(f"Hello {name}")
# greet()
# greet("Kal")


# def train_model(model_name="Random Forest"):
#     print(f"Training {model_name}")
# train_model()
# train_model("Decision Tree")


# def model_result(accuracy,model_name="Default Model"):
#     print(f"{model_name} achieved {accuracy}% accuracy")
# model_result(92, "Random Forest")
# model_result(85)


#keyword arguments
# def model_info(name, accuracy, dataset):
#     print(f"Model: {name}")
#     print(f"Accuracy: {accuracy}%")
#     print(f"Dataset: {dataset}")
# model_info(
#     dataset="Student Performance",
#     name="Random Forest",
#     accuracy=94
# )


# def training_details(model, epochs, learning_rate):
#     print(f"You selected {model} model.")
#     print(f"It has {epochs} number of epochs.")
#     print(f"With learning rate {learning_rate}.")
# training_details(
#     epochs=32,
#     learning_rate=0.5,
#     model="Random forest"
# )


#Function + list + loop
# def check_scores(scores):
#     for score in scores:
#         if score >= 90:
#             print(f"{score} - Excellent")
#         else:
#             print(f"{score} - Needs Improvement")

# accuracies = [92, 78, 95, 84]
# check_scores(accuracies)

# def calculate_average(scores):
#     total=0
#     for s in scores:
#         total+=s
#     avg = total/(len(scores))
#     return avg
# scores = [80, 90, 70, 100, 85]
# average = calculate_average(scores)
# print(average)

# "*args" -- tuples
# def add_numbers(*numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total
# print(add_numbers(10, 20))
# print(add_numbers(10, 20, 30, 40))


#functions + tuple + loops
# def find_average(*scores):
#     total=0
#     for s in scores:
#         total += s
#     avg=total/(len(scores))
#     return avg
# print(find_average(80, 90, 100))
# print(find_average(70, 80, 90, 100))


# "**kwargs" -- dictionaries
# def model_details(**details):
#     print(details)

# model_details(
#     name="Random Forest",
#     accuracy=92,
#     dataset="Student Data"
# )


# def model_details(**details):
#     print(details["name"])
#     print(details["accuracy"])

# model_details(
#     name="Random Forest",
#     accuracy=92
# )


# dictionary + loop + **kwargs
def student_details(**details):
    for key,value in details.items():
        print(f"{key} : {value}")

student_details(
    name="Kal",
    branch="CSE",
    cgpa=8.5
)