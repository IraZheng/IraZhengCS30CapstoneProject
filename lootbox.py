###############################################################################
# lootbox module
###############################################################################
import random


class Lootbox():
    '''Lootbox class'''
    def __init__(self, name, cost, lootTable, inventory, textColours):
        '''
        sets up the class
        name: the name of the lootbox
        cost: the amount of money the lootbox costs in the store
        lootTable: a dict containing items and their chances
        inventory: where items are deposited to
        textColours: a dict used to colour text
        '''
        self.name = name
        self.cost = cost
        self.lootTable = lootTable
        self.inventory = inventory
        self.textColours = textColours
        counter = lootTable.copy()
        for item in counter:
            counter[item] = 0
        self.counter = counter

    
    def Roll(self, amountOfRolls, luck):
        '''
        generates random items based on chances
        amountOfRolls: the number of times it will roll
        '''
        for pull in range(amountOfRolls):
            total = 0
            adjustedTotals = []
            for item in self.lootTable:
                #luck root power to make rare items more likely
                #the most extreme it can go to is even chances for everything
                adjustedChance = self.lootTable[item] ** (1/luck)
                total += 1/adjustedChance
                adjustedTotals.append(1/adjustedChance)
            total2 = 0
            randomEntry = random.random()*total
            #I have to store the adjusted chances in a list b/c I multiplied 
            #random by total
            #enumerate makes the list a dict with keys being its index
            for counter, item in enumerate(self.lootTable):
                total2 += adjustedTotals[counter]
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
        
