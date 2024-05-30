###############################################################################
# Lootbox Module
###############################################################################
import random


class Lootbox():
    def __init__(self, lootTable):
        self.lootTable = lootTable
        counter = lootTable.copy()
        for item in counter:
            counter[item] = 0
        self.counter = counter

    
    def Roll(self, amountOfRolls):
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
                #chance is 1 in Lootbox[item]
                total2 += 1/self.lootTable[item]/total
                #returns lowest rarity
                if randomEntry <= total2:
                    self.Counter(item)
                    break
        print(self.counter)


    def Counter(self, item):
        if item in self.counter:
            self.counter[item] += 1
        else:
            self.counter[item] = 1
        
        