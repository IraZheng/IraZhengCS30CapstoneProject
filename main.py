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
import random

basicItemList = ["common", "uncommon", "rare", "epic", "legend"]
basicChanceList = [59, 25, 10, 5, 1]
rollAmount = 100
# Functions -------------------------------------------------------------------
def shopMenu():
    while True:
        print("Welcome to the shop")
        print("What do you want to do?")
        print("-buy\n-exit")
        choice = input("-").lower()
        if choice == "buy":
            while True:
                try:
                    lootboxAmount = int(input("How many lootboxes do you buy: "))
                except:
                    print("please input a number")
                else:
                    obtainedItems = random.choices(basicItemList, basicChanceList, k=lootboxAmount)
                    itemCounter = {"common": 0, "uncommon": 0, "rare": 0, 
                                   "epic": 0, "legend": 0}
                    for item in obtainedItems:
                        if item in itemCounter:
                            itemCounter[item] += 1
                        else:
                            itemCounter[item] = 1
                    print(itemCounter)
                    break
        elif choice == "exit":
            break
        else:
            print("Please choose one of the options listed above")


# Main ------------------------------------------------------------------------
'''obtainedItems = random.choices(basicItemList, basicChanceList, k=rollAmount)
itemCounter = {}
for item in obtainedItems:
    if item in itemCounter:
        itemCounter[item] += 1
    else:
        itemCounter[item] = 1
print(itemCounter)'''
shopMenu()

