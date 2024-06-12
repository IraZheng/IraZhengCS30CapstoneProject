###############################################################################
#Title: Lootbox Simulator
#Class: CS 30
#Assignment:Capstone Coding Project
#Coder: Ira Zheng
#Version: 2.0
###############################################################################
'''Lootbox Simulator'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
import lootbox
import player
import quests
import random


#for text colors
colours = {"wood": [120, 80, 7],"common": [207, 207, 207], 
           "uncommon": [55, 204, 100], "rare": [36, 96, 199], 
           "epic": [94, 11, 189], "legend": [212, 165, 23], 
           "mythic": [240, 67, 10],"exclusiveB": [46, 53, 71], 
           "exclusiveA": [46, 53, 71]}
#player setup
Player1 = player.Player(10, {"wood": 0, "common": 0, "uncommon": 0, 
                             "rare": 0, "epic": 0, "legend": 0, 
                             "mythic": 0, "exclusiveB": 0, 
                             "exclusiveA": 0}, 
                        colours, [], 1)
#lootbox setup
basicLootbox = lootbox.Lootbox("Basic Lootbox", 1, 
                               {"common": 2, "uncommon": 4, "rare": 8, 
                                "epic": 16, "legend": 32, 
                                "exclusiveB": 1000000}, 
                               Player1.inventory, colours)
advancedLootbox = lootbox.Lootbox("Advanced Lootbox", 5, 
                                  {"uncommon": 2, "rare": 4, "epic": 8, 
                                   "legend": 16, "mythic": 32, 
                                   "exclusiveA": 1000000}, 
                                  Player1.inventory, colours)

#list of lootboxes available in the shop
shopBoxes = [basicLootbox, advancedLootbox]
#setup quests
WoodI = quests.Quest("WoodI", "Collect 10 pieces of wood", 
                     False, 10, 10, "wood")
WoodII = quests.Quest("WoodII", "Collect 100 pieces of wood", 
                      False, 100, 100, "wood")
WoodIII = quests.Quest("WoodIII", "Collect 1000 pieces of wood", 
                       False, 1000, 1000, "wood")
#dict of quests and if they can be taken in the guild
questDict = {WoodI: True, WoodII: True, WoodIII: True}

# Functions -------------------------------------------------------------------
def shopMenu():
    '''Menu of the shop where you buy lootboxes'''
    while True:
        print("\nWelcome to the shop")
        print("-inventory\n-buy\n-exit")
        shopChoice = input("What do you want to do: ").lower()
        if shopChoice == "inventory":
            Player1.printInv()
        elif shopChoice == "buy":
            while True:
                print(f"\nYou have {Player1.coins} coins")
                print(f"{'Cost': <10}{'Item': <20}")
                for box in shopBoxes:
                    print(f"{box.cost: <10}{box.name: <20}")
                print("-back")
                buyChoice = input("What item do you buy: ").lower()
                invalidChoice = True
                if buyChoice == "back":
                    invalidChoice = False
                    break
                for box in shopBoxes:
                    if buyChoice == box.name.lower():
                        invalidChoice = False
                        while True:
                            try:
                                lootboxAmount = int(
                                    input("How many do you buy: "))
                            except:
                                print("please input a number")
                            else:
                                if Player1.coins - lootboxAmount*box.cost >= 0:
                                    box.Roll(lootboxAmount, Player1.luck)
                                    Player1.coins -= lootboxAmount*box.cost
                                else:
                                    print("\nYou do not have enough coins")
                                break
                if invalidChoice:
                    print("Please choose one of the 'Item's listed above")
                else:
                    break
        elif shopChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


def guildMenu():
    '''the place where you do accept quests and gain coins'''
    while True:
        print("\nWelcome to the adventurer's guild")
        print("-inventory\n-accept quests\n" + 
              "-view accepted quests\n-turn in quests\n-exit")
        guildChoice = input("What do you do: ").lower()
        if guildChoice == "inventory":
            Player1.printInv()
        elif guildChoice == "accept quests":
            while True:
                print("\nHere are all the available quests")
                for quest in questDict:
                    if questDict[quest]:
                        print(f"-{quest.name}")
                print("-back")
                questAcceptionChoice = input(
                    "Which quest do you want to take: ").lower()
                invalidChoice = True
                if questAcceptionChoice == "back":
                    invalidChoice = False
                    break
                #ques and not quest b/c it will be one character too long lol
                for ques in questDict:
                    if (Player1.inventory[ques.type] >= ques.requirement):
                        ques.completionStatus = True
                    elif (Player1.inventory[ques.type] < ques.requirement):
                        ques.completionStatus = False
                    if (questAcceptionChoice == ques.name.lower() and 
                        questDict[ques]):
                        while True:
                            print("")
                            ques.printDescription()
                            print("-accept\n-back")
                            acceptionConfirmation = (
                                input("What do you do: ").lower())
                            if acceptionConfirmation == "accept":
                                if len(Player1.acceptedQuests) >= 1:
                                    for accpetedQ in Player1.acceptedQuests:
                                        if accpetedQ.type == ques.type:
                                            print("\nYou cannot have 2 of " + 
                                                 "the same type of quest")
                                            break
                                        else:
                                            print("\nYou have accepted " + 
                                                  f"{ques.name}")
                                            Player1.acceptedQuests.append(ques)
                                            questDict[ques] = False
                                            break
                                else:
                                    print(f"\nYou have accepted {ques.name}")
                                    Player1.acceptedQuests.append(ques)
                                    questDict[ques] = False
                                break
                            elif acceptionConfirmation == "back":
                                break
                            else:
                                print("Please choose one of the " + 
                                      "options listed above")
                        invalidChoice = False
                        break
                if invalidChoice:
                    print("Please choose one of the options listed above")
                else:
                    break
        elif guildChoice == "view accepted quests":
            Player1.viewQuests(questDict)
        elif guildChoice == "turn in quests":
            for quest in Player1.acceptedQuests:
                if quest.completionStatus:
                    #remove items from inventory
                    Player1.inventory[quest.type] -= quest.requirement
                    print(f"\nYou have turned in {quest.requirement} " + 
                          f"{quest.type}")
                    print(f"You have {Player1.inventory[quest.type]} " + 
                          f"{quest.type} left")
                    #rewards
                    Player1.coins += quest.reward
                    print("You have gained " + 
                          f"{quest.reward} coins for completing {quest.name}")
                    print(f"You have {Player1.coins} coins")
                    #makes the quest incomplete
                    quest.completionStatus = False
                    #allows quest to be taken again
                    questDict[quest] = True
                    #removes accepted quests
                    Player1.acceptedQuests.pop()
                else:
                    print(f"\n{quest.name} is " + 
                          f"\033[38;2;{224};{13};{13}m{'incomplete'}\033[0m")
        elif guildChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


def forestMenu():
    '''This is where you gain wood'''
    while True:
        print("\nWelcome to the forest")
        print("-inventory\n-chop wood\n-exit")
        forestChoice = input("What do you do: ").lower()
        if forestChoice == "inventory":
            Player1.printInv()
        elif forestChoice == "chop wood":
            woodAmount = random.randint(1,5)
            Player1.inventory["wood"]+=woodAmount
            print(f"\nYou have gained {woodAmount} wood")
            for quest in Player1.acceptedQuests:
                if (quest.type == "wood" and 
                    Player1.inventory["wood"] >= quest.requirement):
                    quest.completionStatus = True
                    print("You have "+ 
                          f"\033[38;2;{54};{237};{21}m{'completed'}\033[0m" + 
                         f" {quest.name}")
        elif forestChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


def movementMenu():
    '''This menu moves the player to a different location'''
    while True:
        print("\nWhere do you want to go?")
        print("-shop\n-guild\n-forest\n-back")
        movementChoice = input("Where do you want to go: ").lower()
        if movementChoice == "shop":
            shopMenu()
            break
        elif movementChoice == "guild":
            guildMenu()
            break
        elif movementChoice == "forest":
            forestMenu()
            break
        elif movementChoice == "back":
            break
        else:
            print("Please choose one of the options above")


def mainMenu():
    '''the main menu of the game'''
    while True:
        print("\nWhat do you want to do?")
        print("-inventory\n-move\n-quit")
        mainMenuChoice = input("What do you want to do: ").lower()
        if mainMenuChoice == "inventory":
            Player1.printInv()
        elif mainMenuChoice == "move":
            movementMenu()
        elif mainMenuChoice == "quit":
            print("\nYou have quit the game")
            print("Goodbye!")
            break
        else:
            print("Please choose one of the options above")


# Main ------------------------------------------------------------------------
mainMenu()

