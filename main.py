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

#for text colors
colours = {"common": [207, 207, 207], "uncommon": [55, 204, 100],  
      "rare": [36, 96, 199], "epic": [94, 11, 189], 
      "legend": [212, 165, 23], "exclusive": [158, 11, 11]}
#player setup
Player1 = player.Player(10, {"common": 0, "uncommon": 0,  "rare": 0, 
                             "epic": 0, "legend": 0, "exclusive": 0}, 
                        colours, [])
#lootbox setup
basicLootbox = lootbox.Lootbox("Basic Lootbox", 1, 
                               {"common": 2, "uncommon": 4,  "rare": 8, 
                                "epic": 16, "legend": 32, 
                                "exclusive": 1000000}, 
                               Player1.inventory, colours)
#list of lootboxes available in the shop
shopBoxes = [basicLootbox]
#setup quests
WoodI = quests.Quest("WoodI", "Collect 10 pieces of wood", False, 10)
WoodII = quests.Quest("WoodII", "Collect 100 pieces of wood", False, 100)
WoodIII = quests.Quest("WoodIII", "Collect 1000 pieces of wood", False, 1000)
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
                for box in shopBoxes:
                    if buyChoice == box.name.lower():
                        while True:
                            try:
                                lootboxAmount = int(
                                    input("How many do you buy: "))
                            except:
                                print("please input a number")
                            else:
                                if Player1.coins - lootboxAmount*box.cost >= 0:
                                    box.Roll(lootboxAmount)
                                    Player1.coins -= lootboxAmount*box.cost
                                else:
                                    print("\nYou do not have enough coins")
                                break
                if buyChoice == "back":
                    break
                else:
                    print("Please choose one of the 'Item's listed above")
        elif shopChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


def guildMenu():
    '''the place where you do accept quests and gain coins'''
    while True:
        print("\nWelcome to the adventurer's guild")
        print("-accept quests\n-view quests\n-turn in quests\n-exit")
        guildChoice = input("What do you do: ").lower()
        if guildChoice == "accept quests":
            while True:
                print("\nHere are all the available quests")
                for quest in questDict:
                    print(f"-{quest.name}")
                print("-back")
                questAcceptionChoice = input(
                    "Which quest do you want to take: ").lower()
                _invalidChoice = True
                if questAcceptionChoice == "back":
                    _invalidChoice = False
                    break
                for quest in questDict:
                    if questAcceptionChoice == quest.name.lower():
                        print(f"\nYou have accepted {quest.name}")
                        Player1.acceptedQuests.append(quest)
                        questDict[quest] = False
                        _invalidChoice = False
                        break
                if _invalidChoice:
                    print("Please choose one of the options listed above")
                else:
                    break
        elif guildChoice == "view quests":
            print("\nHere are all of your accepted quests:")
            print(f"{'quest':<10}{'status':<10}")
            for quest in Player1.acceptedQuests:
                quest.printDescription()
        elif guildChoice == "turn in quests":
            for quest in range(len(Player1.acceptedQuests)):
                if Player1.acceptedQuests[quest].completionStatus:
                    Player1.coins += Player1.acceptedQuests[quest].reward
                    print("\nYou have gained " + 
                          f"{Player1.acceptedQuests[quest].reward}" + 
                          " coins for completing" + 
                          f" {Player1.acceptedQuests[quest].name}")
                    print(f"You have {Player1.coins} coins")
        elif guildChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


def movementMenu():
    '''This menu moves the player to a different location'''
    while True:
        print("\nWhere do you want to go?")
        print("-shop\n-guild\n-back")
        movementChoice = input("Where do you want to go: ").lower()
        if movementChoice == "shop":
            shopMenu()
            break
        elif movementChoice == "guild":
            guildMenu()
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

