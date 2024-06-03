###############################################################################
# lootbox module
###############################################################################
import random


class Lootbox():
    '''Lootbox class'''
    def __init__(self, lootTable, inventory, textColours):
        '''
        sets up the class
        lootTable: a dict containing items and their chances
        inventory: where items are deposited to
        textColours: a dict used to colour text
        '''
        self.lootTable = lootTable
        self.inventory = inventory
        self.textColours = textColours
        counter = lootTable.copy()
        for item in counter:
            counter[item] = 0
        self.counter = counter

    
    def Roll(self, amountOfRolls):
        '''
        generates random items based on chances
        amountOfRolls: the number of times it will roll
        '''
        for pull in range(amountOfRolls):
            total = 0
            for item in self.lootTable:
                #adds up all of the chances so that they can later be used to 
                #cancel/normalise total2
                total += 1/self.lootTable[item]
            total2 = 0
            randomEntry = random.random()
            for item in self.lootTable:
                #normalises total2
                #chance is around 1 in Lootbox[item]
                total2 += 1/self.lootTable[item]/total
                #returns lowest rarity
                if randomEntry <= total2:
                    self.Counter(item)
                    break
        print("\nYou have obtained:")
        print(f"{'amount':<10}{'item':<10}{'chance':<10}")
        for item in self.counter:
            if self.counter[item] > 0:
                rVal = self.textColours[item][0]
                gVal = self.textColours[item][1]
                bVal = self.textColours[item][2]
                chanceText = f"(1 in {self.lootTable[item]})"
                print(f"{self.counter[item]:<10}" + 
                      f"\033[38;2;{rVal};{gVal};{bVal}m{item:<10}\033[0m" +
                      f"{chanceText:<15}" + 
                      f"{'items':<5}")
            self.counter[item] = 0
            

    def Counter(self, item):
        '''
        stores the number of items in each rarity
        item: the item you are storing
        '''
        #to prevent bugs it will create a key in counter if the key
        #doesn't already exist
        if item in self.counter:
            self.counter[item] += 1
        else:
            self.counter[item] = 1
        #to prevent bugs it will create a key in inventory if the key
        #doesn't already exist
        if item in self.inventory:
            self.inventory[item] += 1
        else:
            self.inventory[item] = 1
        
        