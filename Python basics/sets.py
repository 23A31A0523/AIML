# print("--- Python Sets ---")

# skills = {"Python", "SQL", "Python", "Machine Learning", "SQL"}
# print("Skills:", skills)
# print("Number of skills:", len(skills))

# skills.add("Pandas")
# print("After add:", skills)

# skills.remove("SQL")
# print("After remove:", skills)


# my_skills = {"Python", "SQL", "Git"}
# job_skills = {"Python", "Machine Learning", "SQL", "Pandas"}
# print(my_skills & job_skills)

print("\n--- Set Operations ---")

my_skills = {"Python", "SQL", "Git"}
job_skills = {"Python", "Machine Learning", "SQL", "Pandas"}

# Common skills
print("Common:", my_skills & job_skills)

# All unique skills from both sets
print("All skills:", my_skills | job_skills)

# Skills required by job but missing from my skills
print("Skills to learn:", job_skills - my_skills)