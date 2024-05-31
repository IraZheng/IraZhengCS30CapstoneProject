###############################################################################
# player module
###############################################################################
import itemColor


class Player():
    '''player class'''
    def __init__(self, inventory):
        '''
        initializes class
        inventory: the player's inventory
        '''
        self.inventory = inventory

    
    def printInv(self):
        '''prints the player inventory'''
        print("\nYou have obtained:")
        print(f"{'amount':<10}{'item':<10}{'chance':<10}")
        for item in self.inventory:
            if self.inventory[item] > 0:
                rVal = itemColor.colors[item][0]
                gVal = itemColor.colors[item][1]
                bVal = itemColor.colors[item][2]
                print(f"{self.inventory[item]:<10}" + 
                      f"\033[38;2;{rVal};{gVal};{bVal}m{item:<10}\033[0m" +
                      f"{'items':<5}")