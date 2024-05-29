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

cardList = ["common", "uncommon", "rare"]
chanceList = [90, 9, 1]
# Functions -------------------------------------------------------------------


# Main ------------------------------------------------------------------------
print(random.choices(cardList, chanceList, k=100))

