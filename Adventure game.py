answer = input("Would you like to play this game? (Yes/No): ")
if answer.lower().strip()=="yes":
    answer = input("The game started, there is a road above. would you like to take left or right?: ")
    if answer == "left":
        answer = input("You encountered a monster, would you like to run or take a risk and go to the shore?: ")
        if answer == "run" :
            print("There were boulders below, your speed slowed down & monster caught you: ")
        else:
            print("That was a wise decision. you got a boat at the shore and left the island: ")

    elif answer == "right" :
        print("Monster spewed venom on the track and you were killed: ")
    else:
        print("Invalid choice, you lost!: ")
else:
    print("That's too bad")


