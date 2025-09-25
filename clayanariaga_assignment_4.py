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