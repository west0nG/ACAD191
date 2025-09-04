'''
Weston Guo
ACAD191, FALL 2025
westongu@usc.edu
Lab 1
'''
Speical = ["Homemade Pasta","Kimchi Fried Rice","Dim Sim Set"]
homemadePastaOptions = ["Vegan","Beef","Chicken","Pork"]
kimchiFoodOptions = ["No Spicy","Mild","Spicy","Extra Spicy"]
dimSimOptions = ["Ha Gae","Siu Mai","Cheung Fun","Char Siu Bao"]
restart = True
while restart:
    specialChoice = input("Welcome to the restaurant! What would you like to order? We offer "+Speical[0]+", "+Speical[1]+", and "+Speical[2]+" today.")

    if specialChoice == "Homemade Pasta":
        foodChoice = input("Nice choice! We have "+homemadePastaOptions[0]+", "+homemadePastaOptions[1]+", "+homemadePastaOptions[2]+", and "+homemadePastaOptions[3]+".")
        if foodChoice == "Vegan":
            print("Here is your Vegan Homemade Pasta. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Beef":
            print("Here is your Beef Homemade Pasta. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Chicken":
            print("Here is your Chicken Homemade Pasta. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Pork":
            print("Here is your Pork Homemade Pasta. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        else:
            print("Sorry, we don't have that option. Please try again.")
    elif specialChoice == "Kimchi Fried Rice":
        foodChoice = input("Nice choice! We have "+kimchiFoodOptions[0]+", "+kimchiFoodOptions[1]+", "+kimchiFoodOptions[2]+", and "+kimchiFoodOptions[3]+".")
        if foodChoice == "No Spicy":
            print("Here is your No Spicy Kimchi Fried Rice. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Mild":
            print("Here is your Mild Kimchi Fried Rice. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Spicy":
            print("Here is your Spicy Kimchi Fried Rice. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Extra Spicy":
            print("Here is your Extra Spicy Kimchi Fried Rice. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        else:
            print("Sorry, we don't have that option. Please try again.")
    elif specialChoice == "Dim Sim Set":
        foodChoice = input("Nice choice! We have "+dimSimOptions[0]+", "+dimSimOptions[1]+", "+dimSimOptions[2]+", and "+dimSimOptions[3]+".")
        if foodChoice == "Ha Gae":
            print("Here is your Ha Gae Dim Sim Set. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Siu Mai":
            print("Here is your Siu Mai Dim Sim Set. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Cheung Fun":
            print("Here is your Cheung Fun Dim Sim Set. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        elif foodChoice == "Char Siu Bao":
            print("Here is your Char Siu Bao Dim Sim Set. Enjoy!")
            askRestart = input("Would you like to order anything else? (y/n)")
            if askRestart == "y":
                restart = True
            else:
                restart = False
        else:
            print("Sorry, we don't have that option. Please try again.")
    else:
        print("Sorry, we don't have that option. Please try again.")

