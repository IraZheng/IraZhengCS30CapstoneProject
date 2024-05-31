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

basicLootbox = lootbox.Lootbox({"common": 2, "uncommon": 4,  "rare": 8, 
                                "epic": 16, "legend": 32, 
                                "exclusive": 1000000})


# Functions -------------------------------------------------------------------
def shopMenu():
    '''Menu of the shop where you buy lootboxes'''
    while True:
        print("Welcome to the shop")
        print("What do you want to do?")
        print("-buy\n-exit")
        choice = input("-").lower()
        if choice == "buy":
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

