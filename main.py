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
Player1 = player.Player({"common": 0, "uncommon": 0,  "rare": 0, 
                           "epic": 0, "legend": 0, 
                           "exclusive": 0}, colours)
#lootbox setup
basicLootbox = lootbox.Lootbox({"common": 2, "uncommon": 4,  "rare": 8, 
                                "epic": 16, "legend": 32, 
                                "exclusive": 1000000}, 
                               Player1.inventory, colours)


# Functions -------------------------------------------------------------------
def shopMenu():
    '''Menu of the shop where you buy lootboxes'''
    while True:
        print("\nWelcome to the shop")
        print("What do you want to do?")
        print("-inventory\n-buy\n-exit")
        choice = input("-").lower()
        if choice == "inventory":
            Player1.printInv()
        elif choice == "buy":
            while True:
                try:
                    lootboxAmount = int(
                        input("How many lootboxes do you buy: "))
                except:
                    print("please input a number")
                else:
                    basicLootbox.Roll(lootboxAmount)
                    break
        elif choice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


# Main ------------------------------------------------------------------------
shopMenu()

