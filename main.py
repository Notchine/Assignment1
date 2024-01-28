#establishing values/inventory stuff
hasBook = False
hasFood = False
#value changes when vampire dies, allows player to leave front door again after it shuts
vampireDefeated = False
#inventory list which is empty to begin with, fills up with stuff later on
inventory = []


#opening, mosting just set dressing with no real key info to keep track of this early in the game
print("You stand at the precipice of the vampires castle, the screeching ")
print("of bats echoing as the massive front door slides open on its own.")
print("You have one single task. Defeat the vampire within, finally setting your village free from his darkness.")
#blank text line for separation between the dialogue, and actual interaction/gameplay
print("")
print("You can either ENTER the caslte, or OBSERVE your surroundings before entering.")
print("You can also check your inventory at any time by typing INVENTORY in the chatbox.")
#BIG MAIN GAME LOOP
while not vampireDefeated:
    #variable for player input,
    print("")
    choice = input("What will you do? (Use the capitalised words above as your inputs for the player! Also, you can OBSERVE in any area, even if not mentioned.) ")

    #Converts input to uppercase
    choice = choice.upper()

    if choice == "ENTER":
        print("You step into the dimly lit castle, the colossal door shutting slowly behind you.")
        print("Close to the door, there are a series of loose notes laying on a floor which seem to catch the eye, leading to a room on the left.")
        print("There is also a door to the right, but it seems significantly less intersting to the eye.")

        # Door choice loop
        while True:
            door_choice = input("Which door will you choose? (LEFT or RIGHT): ")
            door_choice = door_choice.upper()
            if door_choice == "LEFT":
                print("You enter the left door and find yourself in a grand library, thick cobwebs coating every inch.")
                print("There's a strangely inviting dusty book on the table. Do you READ it or LEAVE the library?")

                # Library choice loop
                while True:
                    library_choice = input("Your choice (READ or LEAVE): ")
                    library_choice = library_choice.upper()
                    if library_choice == "READ" and hasBook == False:
                        print("The handy book seems to cover the weaknesses of vampires. How handy!")
                        print("After a quick read, you learn to harness the arcane powers of sunlight.")
                        print("Obtained: DAZZLING SUNLIGHT")
                        inventory.append("DAZZLING SUNLIGHT")
                        hasBook = True
                        print("You decide to leave.")
                        break  # Exit the library choice loop
                    elif library_choice == "READ" and hasBook == True:
                        print("You have already read this book. You decide to leave.")
                        break
                    elif library_choice == "LEAVE":
                        print("You decide to leave the library and continue your exploration.")
                        break  # Exit the library choice loop
                    else:
                        print("Invalid choice.")

            elif door_choice == "RIGHT":
                print("You enter the right door and find yourself in a pristine dining room. Despite it's perfectly maintained appearance, you seem to be alone.")
                print("There are piles of FOOD laying on the table in near endless supply, ")

                # Dining Hall choice loop
                while True:
                    print("")

                    break #Exit the dining hall

                break  # Exit the door choice loop
    elif choice == "OBSERVE":
        print("The castle stands tall, dauntingly casting a massive shadow over your entire villaige. ")
        print("Despite the cryptic, abandoned exterior, the visible interior seems to be surprisingly well maintained.")


    elif choice == "INVENTORY":
        print("In your inventory, you have: ", inventory)

    else:
        print("You nervously stand at the entrance, unsure what to do.")


