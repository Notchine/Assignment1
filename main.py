#establishing values/inventory stuff
#value changes when vampire dies, allows player to leave front door again after it shuts
vampireDefeated = False
#inventory list which is empty to begin with, fills up with stuff later on
inventory = []


#opening, mosting just set dressing with no real key info to keep track of this early in the game
print("You stand at the precipice of the vampires castle, the screeching ")
print("of bats echoing as the door slides open on its own.")
print("You have one single task. Defeat the vampire within, finally setting your village free from his darkness.")
#blank text line for separation between the dialogue, and actual interaction/gameplay
print("")
print("You can either ENTER the caslte, or OBSERVE your surroundings before entering.")
#BIG MAIN GAME LOOP
while not vampireDefeated:
    #variable for player input,
    choice = input("What will you do? (Use the capitalised words above as your inputs for the player!) ")
else:
    print("You nervously stand at the entrance, unsure what to do.")