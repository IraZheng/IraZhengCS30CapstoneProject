###############################################################################
# player module
###############################################################################
class Player():
    '''player class'''
    def __init__(self, inventory, textColours):
        '''
        initializes class
        inventory: the player's inventory
        textColours: a dict used to colour text
        '''
        self.inventory = inventory
        self.textColours = textColours

    
    def printInv(self):
        '''prints the player inventory'''
        print("\nIn your inventory you have:")
        print(f"{'amount':<10}{'item':<10}")
        for item in self.inventory:
            if self.inventory[item] > 0:
                rVal = self.textColours[item][0]
                gVal = self.textColours[item][1]
                bVal = self.textColours[item][2]
                print(f"{self.inventory[item]:<10}" + 
                      f"\033[38;2;{rVal};{gVal};{bVal}m{item:<10}\033[0m" +
                      f"{'items':<5}")