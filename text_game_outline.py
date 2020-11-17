# CODE OUTLINE

# Ask the user if they want to enter the dungeon 
enter_dungeon_decision = input("Would you like to enter the dungeon? Type Yes or No: ")


# input check
while (enter_dungeon_decision.lower() != 'yes' and enter_dungeon_decision.lower() !='no'):
    print("Invalid input, please type Yes or No")
    enter_dungeon_decision = input("Would you like to enter the dungeon? Type Yes or No: ")



# entered the dungeon
if (enter_dungeon_decision.lower() == 'yes'):
    print("You have entered the dungeon")

    # left or right decision
    path_decision = input('You have reached a dead end. Would you like to turn left or right?: ')

    # LEFT PATH SCENARIO
    # user turned left
    if (path_decision.lower() =='left'):
        print('You turned left and entered a mysterious room')
    
        # prompt user to take a sword or shield 
        item_decision = input('You found a shield and a sword but you can only pick one. Which one would you like to pick up? Please type sword or shield: ')
        
        # SWORD SCENARIO
        # user took the sword 
        if (item_decision.lower() == 'sword'):
            print("You took the sword.")
            # update user's attack power and add item to the inventory
            # FILL IN WITH CODE


            # prompt user if they would like to enter another room or exit the cave
            next_decision = input('Would you like to enter another room or exit the cave? Type room or exit: ')
            
            # user enters a room and encounters a monster 
            if (next_decision.lower() == 'room'):
                print('You entered the room and encountered a monster with 10 attack power and 50 hp.')

                # Prompt the user if they would like to fight or flee 
                fight_flight_decision = input('Your attack power is ' + str(user_attack_power) + ' and your hp is ' + str(user_health) + '. Would you like to fight or flee? Type fight or flee: ')
                
                # User picked fight
                if(fight_flight_decision.lower() == 'fight'):
                    print("You decided to fight the monster.")
                    # FILL IN WITH CODE

                # Assume the user decided to flee
                else:
                    print('You have fled safely with ' + str(user_health) + 'HP left. Time to leave the cave before I get eaten by another monster.Bye! ')
           
            # Assume the user exits the cave 
            else:
                print('You exited the cave alive. Game over. Bye!')

        # SHIELD SCENARIO
        # Assume the user picked up the shield 
        else:
            print('You picked up the shield')
            # Increase user's health and add shield to the inventory
            # FILL IN WITH CODE 


            # prompt user if they want to enter another room or exit the cave (end game)
            next_decision = input('Would you like to enter another room or exit the cave? Type room or exit: ')

            # User enters a room and encounters a monster but runs away
            if (next_decision.lower() == 'room'):
                print('You have encountered a monster but you do not have a weapon. Time to run away! Bye!')
            
            # Assume the user exits the cave 
            else:
                print('You exited the cave alive. Game over. Bye!')

    # RIGHT PATH SCENARIO
    # Assume the user turned right 
    else:
        print('You turned right and entered a mysterious room.')

        # User finds a pile of coins 
        decision = input('You found a pile of coins. Would you like to pick them up? Type yes or no: ')

        # User takes the pile of coins 
        if (decision.lower() =='yes'):
            print("You picked up all the coins and stored them in your bag.")

            # User enters a shop to buy items
            # FILL IN WITH CODE 
        
        # Assume the user did not pick up the coins 
        else:
            print("You decided not to pick up the coins and soon starved to death because you could not buy anything from the nearby shop. Game over!")

# Assume that the user did not enter the dungeon 
else:
    print("You did not enter the dungeon. Goodbye!")
