'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 1
'''

userName = input("Hello, whose BMI shall I calculate? (Enter nothing to exit) ")
while userName != "":
    print(f"Okay first I need {userName}'s height. I'll take it in feet and inches. ")
    userHeightFeet = input("Feet First...")
    userHeightInches = input("Now Inches...")
    print(f"Thanks. Now I need {userName}'s weight in pounds. ")
    userWeight = float(input(f"Please enter {userName}'s weight in pounds"))

    userOverallHeightInInches = int(userHeightFeet) * 12 + int(userHeightInches)
    if int(userOverallHeightInInches) < 0:
        print("Invalid input. Please try again.")
    else:
        print("Your total height in inches is " + str(userOverallHeightInInches))

    userOverallHeightInMeters = float(userOverallHeightInInches) / 39.37
    print("Your total height in meters is " + str(f"{userOverallHeightInMeters:.2f}"))

    userBMI = float(userWeight * 0.453592) / (float(userOverallHeightInMeters) ** 2)
    print(f"{userName}'s BMI is {userBMI:.2f}")
    userName = input("Hello, whose BMI shall I calculate? (Enter nothing to exit) ")




