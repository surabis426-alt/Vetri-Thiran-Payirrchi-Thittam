# FitBuddy - Simple Fitness Plan Generator

print("================================")
print("        WELCOME TO FITBUDDY")
print("   FITNESS PLAN GENERATOR")
print("================================")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nChoose your fitness goal:")
print("1. General Fitness")
print("2. Strength")
print("3. Flexibility")

choice = input("Enter your choice (1/2/3): ")

print("\nChoose your fitness level:")
print("1. Beginner")
print("2. Intermediate")

level = input("Enter your level (1/2): ")

print("\n--------------------------------")
print("        YOUR FITBUDDY PLAN")
print("--------------------------------")

print("Name:", name)
print("Age:", age)

if choice == "1":

    print("Goal: General Fitness")

    if level == "1":
        print("\nExercises:")
        print("- Walking - 20 minutes")
        print("- Squats - 2 sets")
        print("- Wall Push-ups - 2 sets")
        print("- Stretching - 10 minutes")

    else:
        print("\nExercises:")
        print("- Brisk Walking - 30 minutes")
        print("- Squats - 3 sets")
        print("- Push-ups - 3 sets")
        print("- Plank - 20 seconds")

elif choice == "2":

    print("Goal: Strength")

    if level == "1":
        print("\nExercises:")
        print("- Squats - 2 sets")
        print("- Wall Push-ups - 2 sets")
        print("- Glute Bridges - 2 sets")

    else:
        print("\nExercises:")
        print("- Squats - 3 sets")
        print("- Push-ups - 3 sets")
        print("- Lunges - 2 sets")
        print("- Plank - 30 seconds")

elif choice == "3":

    print("Goal: Flexibility")

    print("\nExercises:")
    print("- Shoulder Stretch - 30 seconds")
    print("- Hamstring Stretch - 30 seconds")
    print("- Butterfly Stretch - 30 seconds")
    print("- Light Walking - 15 minutes")

else:
    print("Invalid choice!")

print("\n--------------------------------")
print("Health Tips:")
print("- Drink enough water")
print("- Eat balanced meals")
print("- Get enough sleep")
print("- Warm up before exercise")
print("--------------------------------")

print("\nThank you for using FitBuddy!")
