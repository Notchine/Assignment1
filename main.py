import random
#establishing values/inventory stuff
hasBook = False
hasFood = False
#value changes when vampire dies, allows player to leave front door again after it shuts
vampireDefeated = False
#inventory list which is empty to begin with, fills up with stuff later on
inventory = []
#Name dictionary thing (randomly pick one of them to be player)
nameList = {"Daniel": None, "John": None, "Tyler": None, "Marcel": None, "Markus": None, "Anthony": None, "Ethyn": None, "David": None}
ranName = random.choice(list(nameList.keys()))

#cool function for killing vampire
def killVampire():
    vampireDefeated = True
    print("With a mighty blast of concentrated sunlight, the vampire is instantly obliterated in a blinding flash.")
    print("When your vision returns, all that remains is their dark cloak, resting silently in a pile of ashes.")
    print("Congratulations, " + ranName + " You have set your village free from the eternal darkness of the evil vampire!")
    input("THE END (Thanks for Playing!)")
    quit()


#opening, mosting just set dressing with no real key info to keep track of this early in the game
print("Your name is: " + ranName)
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
    choice = input("What will you do? (Use the capitalised words above as your inputs for the player! Also, you can OBSERVE or check your INVENTORY in any area, even if not mentioned.) ")

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
                    library_choice = input("Your choice? (READ or LEAVE): ")
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
                    elif library_choice == "INVENTORY":
                        print("In your inventory, you have: ", inventory)

                    elif library_choice == "INVENTORY":
                        print("In your inventory, you have: ", inventory)

                    else:
                        print("Invalid choice.")


            elif door_choice == "RIGHT":
                print("You enter the right door and find yourself in a pristine dining room. Despite it's perfectly maintained appearance, you seem to be alone.")
                print("There are piles of FOOD laying on the table in near endless supply, and a sleeping ZOMBIE servant laying on the ground protecting a door. It would be wise to not approach before being well armed.")

                # Dining Hall choice loop
                while True:
                    dining_choice = input("Your choice? (FOOD, ZOMBIE or LEAVE)")
                    dining_choice = dining_choice.upper()

                    if dining_choice == "FOOD" and hasFood == False:
                        print("You take a heaping FOOD which, upon closer inspection, seems to be rotten and completely inedible.")
                        print("Obtained: ROTTEN MEAT")
                        inventory.append("ROTTEN MEAT")
                        hasFood = True
                        print("The ROTTEN MEAT squelches loudly in your pockets.")
                    elif dining_choice == "FOOD" and hasFood == True:
                        print("You already have more rotten meat than your stomach can handle.")
                    elif dining_choice == "ZOMBIE" and hasFood == False:
                        print("As you get closer to the zombie, he springs to life like a machine, grunting loudly at you.")
                        print("He seems to be eying you like a piece of meat, and only reacts when you enter a certain radius near the door.")
                        print("It might be a good idea to back off for now.")
                        print("You sprint back to the previous room, out of fear.")
                        break #its OVER
                    elif dining_choice == "ZOMBIE" and hasFood == True:
                        print("As you get closer to the zombie, he springs to life like a machine, a deeply hungry look in his dead eyes.")
                        print("On reflex, you fling the food towards the zombie, distracting him completely as he hunches over and chows down.")
                        print("Seems like he'll be occupied for a while, so you move ahead to the next room.")
                        input("Press Enter to continue...")
                        print(" ")

                   #Dungeon choice loop
                        while True:
                            if "DAZZLING SUNLIGHT" in inventory:
                                print("With the sound of the zombies gnashing getting quieter, you descend a series of stairs into pure darkness.")
                                print("Thanks to your DAZZLING SUNLIGHT, you are able to make your way throuhg the abandoned dungeons.")
                                print("As you trudge through the faded, blood splattered repeating series of cells, you make out what seems to be a rudimentary elevator.")
                                print("It seems to activate with a LEVER which sticks out prominently.")
                                dungeon_choice = input("Will you pull the LEVER or EXIT from where you came?")
                                dungeon_choice = dungeon_choice.upper()

                                if dungeon_choice == "LEVER":
                                    print("")
                                    #THE VAMPIRES LAIR
                                    while True:
                                        if "DAZZLING SUNLIGHT" in inventory:
                                            print("After the elevator ride up, you are face to face with vampire who almost immediately tries to syphon your life force upon seeing you enter his lair.")
                                            print("Before he can fly towards you, you tear open your dusty book to unleash DAZZLING SUNLIGHT, instantly petrifying the vampire in a glorious blast of light!")
                                            input("Press Enter to Continue...")
                                            print(" ")
                                            killVampire()
                                        if "DAZZLING SUNLIGHT" not in inventory:
                                            print("After the elevator ride up, you are presented with the eagarly awaiting vampire who quickly drains your life energy. YOU DIED.")
                                elif dungeon_choice == "EXIT":
                                    print("You scamper out of the room, quickly heading back up the stairs and passing the still distracted zombie.")
                                    break

                                elif door_choice == "INVENTORY":
                                    print("In your inventory, you have: ", inventory)
                                else:
                                    print("Invalid choice.")

                            if "DAZZLING SUNLIGHT" not in inventory:
                                print("With the sound of the zombies gnashing getting quieter, you descend a series of stairs into pure darkness. The abyss is deafeningly dark, and you can't even see your own hands infront of your face.")
                                print("With no way to see, you stumble your way back up the stairs.")
                                print(" ")
                                break

                            elif door_choice == "INVENTORY":
                                print("In your inventory, you have: ", inventory)
                            else:
                                print("Invalid choice.")

                    elif dining_choice == "LEAVE":
                        print("You leave the dining hall, exiting back to the entrance of the castle.")
                        break  # Exit the dining hall
                    elif door_choice == "INVENTORY":
                        print("In your inventory, you have: ", inventory)
                    else:
                        print("Invalid choice.")

            elif door_choice == "INVENTORY":
                print("In your inventory, you have: ", inventory)

            else:
                print("Invalid choice.")
    elif choice == "OBSERVE":
        print("The castle stands tall, dauntingly casting a massive shadow over your entire village. ")
        print("Despite the cryptic, abandoned exterior, the visible interior seems to be surprisingly well maintained.")

    elif choice == "INVENTORY":
        print("In your inventory, you have: ", inventory)

    else:
        print("You nervously stand at the entrance, unsure what to do.")

