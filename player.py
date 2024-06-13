###############################################################################
# player module
###############################################################################
class Player():
    '''player class'''
    def __init__(self, coins, inventory, textColours, acceptedQuests, luck):
        '''
        initializes class
        coins: the amount of couns the player has
        inventory: the player's inventory
        textColours: a dict used to colour text
        acceptedQuests a list of accepted quests
        luck: the luck of the player
        '''
        self.coins = coins
        self.inventory = inventory
        self.textColours = textColours
        self.acceptedQuests = acceptedQuests
        self.luck = luck
        self.equipped = "none"

    
    def printInv(self, itemStrength):
        '''
        prints the player inventory
        itemStrength: the strength of the item
        '''
        while True:
            print("\nIn your inventory you have:")
            print(f"{self.coins} coins")
            print(f"{'amount':<10}{'item':<10}")
            for item in self.inventory:
                if self.inventory[item] > 0:
                    rVal = self.textColours[item][0]
                    gVal = self.textColours[item][1]
                    bVal = self.textColours[item][2]
                    print(f"{self.inventory[item]:<10}" + 
                          f"\033[38;2;{rVal};{gVal};{bVal}m{item:<10}\033[0m" +
                          f"{'items':<5}")
            print("-back")
            if self.equipped != "none":
                rVal = self.textColours[self.equipped][0]
                gVal = self.textColours[self.equipped][1]
                bVal = self.textColours[self.equipped][2]
                print("You currently have " + 
                      f"\033[38;2;{rVal};{gVal};{bVal}m{self.equipped}" + 
                      "\033[0m equipped")
            else:
                print(f"You currently have {self.equipped} equipped")
            print("it has a stength of " + 
                  f"{itemStrength[self.equipped][0]}-" + 
                  f"{itemStrength[self.equipped][1]}")
            equipChoice = input("What do you equip: ")
            if equipChoice == 'wood':
                print("\nYou cannot equip wood")
            elif ((equipChoice in self.inventory) and 
                  (self.inventory[equipChoice] > 0)):
                rVal = self.textColours[equipChoice][0]
                gVal = self.textColours[equipChoice][1]
                bVal = self.textColours[equipChoice][2]
                print("\nYou have equipped " + 
                      f"\033[38;2;{rVal};{gVal};{bVal}m{equipChoice}\033[0m")
                self.equipped = equipChoice
                print("it has a stength of " + 
                      f"{itemStrength[self.equipped][0]}-" + 
                      f"{itemStrength[self.equipped][1]}")
                break
            elif equipChoice == "back":
                break
            else:
                print("Please choose one of the options listed above")

    def viewQuests(self, questDict):
        '''
        allows player to view and abandon quests
        questDict: the dictionary that the quest function uses
        '''
        while True:
            print("\nHere are all of your accepted quests:")
            for quest in self.acceptedQuests:
                print("")
                quest.printDescription()
            print("-back")
            viewChoice = input("Which quest do you view: ").lower()
            invalidChoice = True
            if viewChoice == "back":
                invalidChoice = False
                break
            for quest in self.acceptedQuests:
                if viewChoice == quest.name.lower():
                    invalidChoice = False
                    while True:
                        print("")
                        quest.printDescription()
                        print("-abandon\n-back")
                        abandonChoice = input("What do you do: ").lower()
                        if abandonChoice == 'abandon':
                            self.acceptedQuests.remove(quest)
                            questDict[quest] = True
                            break
                        elif abandonChoice == 'back':
                            break
                        else:
                            print("Please choose one of the above options")
                    break
            if invalidChoice:
                print("Please choose one of the " + 
                       "quests listed above or 'back'")
            else:
                break

