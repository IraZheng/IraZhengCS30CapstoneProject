###############################################################################
#Title: Lootbox Simulator
#Class: CS 30
#Assignment:Capstone Coding Project
#Coder: Ira Zheng
#Version: 1.0
###############################################################################
'''Lootbox Simulator'''
###############################################################################
# Imports and Global Variables ------------------------------------------------
import lootbox
import player

#for text colors
colours = {"common": [207, 207, 207], "uncommon": [55, 204, 100],  
      "rare": [36, 96, 199], "epic": [94, 11, 189], 
      "legend": [212, 165, 23], "exclusive": [158, 11, 11]}
#player setup
Player1 = player.Player(10, {"common": 0, "uncommon": 0,  "rare": 0, 
                             "epic": 0, "legend": 0, "exclusive": 0}, 
                        colours)
#lootbox setup
basicLootbox = lootbox.BasicLootbox(Player1.inventory, colours)
#list of lootboxes available in the shop
shopBoxes = [basicLootbox]


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
                    print(f"{box.cost: <10}{str(box): <20}")
                print("-back")
                buyChoice = input("-").lower()
                for box in shopBoxes:
                    if buyChoice == str(box).lower():
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
                    print("Please choose one of the items listed above")
        elif shopChoice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


# Main ------------------------------------------------------------------------
shopMenu()

