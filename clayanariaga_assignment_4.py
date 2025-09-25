# College Life Game
# By: Clayan Ariaga

# Step 1: Foundation Setup
student_name = "Clayan Ariaga"
current_gpa = 3.2      # float between 1.0 and 4.0
study_hours = 20       # integer
social_points = 50     # integer
stress_level = 30      # integer between 0 and 100

print(f"Welcome {student_name} to the College Life Game")
print("Here are your starting stats:")
print(f"GPA: {current_gpa}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")


# Step 2: Course Planning Decision
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    # comparison operators
    if current_gpa >= 2.0:
        study_hours += 5
        stress_level -= 5
        print("Light load: less stress, extra time to study.")
    else:
        stress_level += 5
        print("Even with a light load, low GPA will make it tough.")
elif choice == "B":
    study_hours += 10
    stress_level += 5
    print("Standard load: balanced but challenging.")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours += 15
        stress_level += 15
        print("Heavy load with strong GPA: you manage, but it’s stressful.")
    else:
        current_gpa -= 0.2
        stress_level += 25
        print("Heavy load with lower GPA: stress rises, GPA will drop.")
else:
    # handles invalid input
    print("Invalid input. Defaulting to standard load.")
    study_hours += 10
    stress_level += 5

    # Step 3: Study Strategy Decision
    study_options = ["Programming", "Math", "English", "History"]

    print("Pick a subject to focus your study hours on:")
    print(study_options)
    study_choice = input("Your choice: ")

    if study_choice not in study_options:  # membership operator
        print("Invalid")
    else:
        if study_choice == "Programming" and current_gpa < 3.0:  # logical operator
            current_gpa += 0.3
            print("Programming focus helps raise your GPA!")
        elif study_choice == "Math" or study_choice == "English":
            current_gpa += 0.1
            social_points -= 5
            print(f"Studying {study_choice} boosted GPA but cut into your social life.")
        else:
            social_points += 5
            print(f"Studying {study_choice} gave you balance and better connections.")

# Step 4: Final Semester Assessment
print(" Final Semester Assessment ")

# Identity operator
if type(current_gpa) is float:
    print("Confirmed: GPA is a float type.")
elif type(current_gpa) is not float:
    print("Invalid")

# ifs for endings
if current_gpa >= 3.5:
    if stress_level < 50:
        if social_points>=40:
            ending = "Dean’s List with no help"
        else:
            ending = "Dean’s List with help"
    else:
        ending = "High GPA but too stressed: burnout ending."
elif current_gpa < 2.0:
    if social_points < 30:
        if stress_level>60:
            ending = "complete burnout: low gpa, low support, high stress."
        else:
            ending = "Academic Probation: low GPA and no support system."
    else:
        ending = "Probation"
else:
    if study_hours > 25 and stress_level < 60:
        ending = "Balanced Success: steady GPA and manageable stress."
    else:
        ending = "Average Semester: you stayed afloat."

print(f"Final Stats for {student_name}:")
print(f"GPA: {round(current_gpa,2)}, Study Hours: {study_hours}, Social Points: {social_points}, Stress Level: {stress_level}")
print(f"Ending: {ending}")