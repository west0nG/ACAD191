'''
Weston Guo
ACAD 191, Fall 2025
westongu@usc.edu
Homework 3
'''

monthDictionary = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

Calender = {}
for month in monthDictionary:
    Calender[month] = []
    for day in range(1, monthDictionary[month] + 1):
        Calender[month].append("")

#print(Calender)

userInputDate = input("Enter a date for a holiday(for example 'July 1'): ")



while userInputDate != "":
    parts = userInputDate.split()
    if len(parts) != 2:
        print("I don't see a good input there!")

    else:
        month, day = parts
        if month in monthDictionary:
            if int(day) in range(1, monthDictionary[month] + 1):
                userInputHoliday = input(f"What happens on {month} {day}? ")
                Calender[month][int(day) - 1] = userInputHoliday
            elif int(day) > monthDictionary[month]:
                print(f"That month only has {monthDictionary[month]} days!")
            else:
                print("I don't see a good input there!")
        else:
            print(f"I don't know about the month '{month}'")
    userInputDate = input("Enter a date for a holiday(for example 'July 1': ")

# print the calender when it's not empty
for month in Calender:
    for day in range(1, monthDictionary[month] + 1):
        if Calender[month][day - 1] != "":
            print(f"{month} {day}: {Calender[month][day - 1]}")

# save the file
fileName = input("Enter the file name to save your calender: ")

if fileName != "":
    file = open(fileName + ".txt", "w")
    for month in Calender:
        for day_index, day_content in enumerate(Calender[month]):
            if day_content != "": 
                file.write(f"{month} {day_index + 1}: {day_content}\n")
    file.close()
    print(f"Calendar saved to {fileName}")


print("Goodbye!")


