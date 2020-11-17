
# user inventory
inventory = []

# coins
coins = 0

# monster stats
monster_hp = 50
monster_attack = 10


# Welcome the user and ask for their name and character atrributes 
user_name = input("What is your name adventurer?: ")
print("Greetings " + user_name)

# Set character attributes 
user_attack_power = input("Set your attack power: ")

# implement input check 
while (user_attack_power.isalpha()):
    print("invalid input, please enter a number!")
    user_attack_power = input("Set your attack power: ")

user_attack_power = int(user_attack_power)

print("You have an attack power of " + str(user_attack_power))

user_health = input("Set your hp: ")

# implement input check 
while (user_health.isalpha()):
    print("invalid input, please enter a number!")
    user_health= input("Set your hp: ")

user_health = int(user_health)

print("You have " + str(user_health) + " hp")

# Ask the user if they want to enter the dungeon 
enter_dungeon_decision = input("Would you like to enter the dungeon? Type Yes or No: ")


# input check
while (enter_dungeon_decision.lower() != 'yes' and enter_dungeon_decision.lower() !='no'):
    print("Invalid input, please type Yes or No")
    enter_dungeon_decision = input("Would you like to enter the dungeon? Type Yes or No: ")

# OUTLINE 

# enter the dungeon
if (enter_dungeon_decision.lower() == 'yes'):
    print("You have entered the dungeon")

    # left or right decision
    path_decision = input('You have reached a dead end. Would you like to turn left or right?: ')
    
    # user turns left
    if (path_decision.lower() == 'left'):
        print('You turned left and entered a mysterious room')
        
        # prompt user to take a sword or shield 
        item_decision = input('You found a shield and a sword but you can only pick one. Which one would you like to pick up? Please type sword or shield: ')

        # add a sword to the player's inventory and increase their attack power by 10 points
        if (item_decision.lower() == 'sword'):
            print("You took the sword.")
            # update the user's attack power
            user_attack_power += 10
            # add item to the player's inventory
            inventory.append('sword')
            # display player stats
            print('Increased attack power by 10. Your current attack power is ' + str(user_attack_power))
            # display inventory
            print('Current items in your inventory: ')
            print(inventory)

            # prompt user if they want to enter another room or exit the cave (end game)
            next_decision = input('Would you like to enter another room or exit the cave? Type room or exit: ')
            
            # user enters a room and encounters a monster
            if (next_decision.lower() == 'room'):
                print('You entered the room and encountered a monster with 10 attack power and 50 hp.')
                # fight or flight?
                fight_flight_decision = input('Your attack power is ' + str(user_attack_power) + ' and your hp is ' + str(user_health) + '. Would you like to fight or flee? Type fight or flee: ')
                
                if(fight_flight_decision.lower() == 'fight'):
                    print("You decided to fight the monster.")
                    user_health -= monster_attack
                    monster_hp -= user_attack_power
                    print('You attacked the monster. Your HP: ' + str(user_health) + ' Monster HP: ' + str(monster_hp))
                    
                    # check if the user or the monster died 
                    if (user_health <= 0):
                        print('You are dead. Game over!')
                    elif (monster_hp <= 0):
                        print('The monster has been slain. You won the game!')
                    else:
                        while (user_health > 0):
                            # user can keep fighting or flee 
                            fight_flee = input('Fight or flee: ')
                            if (fight_flee.lower() == 'fight'):
                                user_health -= monster_attack
                                monster_hp -= user_attack_power
                                print('You attacked the monster. Your HP: ' + str(user_health) + ' Monster HP: ' + str(monster_hp))
                                if (user_health <= 0):
                                    print('You are dead. Game over!')
                                    exit()
                                elif (monster_hp <= 0):
                                    print('The monster has been slain. You won the game!')
                                    exit()
                            # assume that the user has fled, so end game
                            else:
                                print('You have fled safely with ' + str(user_health) + 'HP left. Time to leave the cave before I get eaten by another monster. Bye! ')
                                exit()
                
                # assume the user fled; exit the game 
                else:
                    print('You have fled safely with ' + str(user_health) + 'HP left. Time to leave the cave before I get eaten by another monster.Bye! ')

            # assume user exits the cave 
            else:
                print('You exited the cave alive. Game over. Bye!')

        # assume that the user picks up the shield 
        else:
            print('You picked up the shield')
            user_health += 50
            # add shield to the inventory
            inventory.append('shield')
            # display player stat
            print('Increased HP by 50. Your current HP is ' + str(user_health))
            # display inventory
            print('Current items in your inventory: ')
            print(inventory)

            # prompt user if they want to enter another room or exit the cave (end game)
            next_decision = input('Would you like to enter another room or exit the cave? Type room or exit: ')
            
            # user enters a room and encounters a monster
            if (next_decision.lower() == 'room'):
                print('You have encountered a monster but you do not have a weapon. Time to run away! Bye!')
            
            # assume user exits the cave for any other input
            else:
                print('You exited the cave alive. Game over. Bye!')

    # assume that the user turns right 
    else:
        print('You turned right and entered a mysterious room.')
        
        # found a pile of coins, prompt user what to do
        decision = input('You found a pile of coins. Would you like to pick them up? Type yes or no: ')
        if (decision.lower() =='yes'):
            print("You picked up all the coins and stored them in your bag.")
            coins += 40
            print('You now have ' + str(coins) + ' coins.')
            print('Afterwards, you entered a shop selling swords(5 coins), armor (10 coins), and health potions (5 coins).')
            
            while (coins > 0):
                next_decision = input("What would you like to buy? Type sword, armor, health potion, or exit when you are done: ")

                if (next_decision.lower() == 'sword'):
                    difference = coins - 5
                    if (difference > 0):
                        coins -= 5
                        print('You purchased a sword. You have ' + str(coins) + ' coins left.')
                        print('inventory: ')
                        inventory.append('sword')
                        print(inventory)
                    else:
                        # No money left 
                        print("You do not have enough coins. You are officially broke. Time to leave the dungeon. Bye! ")
                        exit()

                elif (next_decision.lower() =='armor'):
                    difference = coins - 10
                    if (difference > 0):
                        coins -= 10
                        print('You purchased armor. You have ' + str(coins) + ' coins left.')
                        print('inventory: ')
                        inventory.append('armor')
                        print(inventory)
                    else:
                        # No money left 
                        print("You do not have enough coins. You are officially broke. Time to leave the dungeon. Bye! ")
                        exit()
                
                elif (next_decision.lower() =='health potion'):
                    difference = coins - 5
                    if (difference > 0):
                        coins -= 5
                        print('You purchased a health potion. You have ' + str(coins) + ' coins left.')
                        print('inventory: ')
                        inventory.append('health potion')
                        print(inventory)
                    else:
                        # No money left 
                        print("You do not have enough coins. You are officially broke. Time to leave the dungeon. Bye! ")
                        exit()
                # assume the user has typed exit 
                else:
                    print('You have exited the shop and decided to go home because you are hungry. Bye!')
                    exit()
        
        # assume the user did not want to pick up the coins
        else:
            print("You decided not to pick up the coins and soon starved to death because you could not buy anything from the nearby shop. Game over!")

# Assume that the user did not enter the dungeon 
else: 
    print("You did not enter the dungeon. Goodbye!")