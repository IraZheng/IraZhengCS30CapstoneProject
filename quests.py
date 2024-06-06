###############################################################################
# player module
###############################################################################
class Quest():
    "quest class"
    def __init__(self, name, description, completionStatus, reward):
        '''
        sets up the quest class
        name: the name of the quest
        description: the description of the class
        completionStatus: a bool of whether or not the quest is complete
        reward: the number of coins you get after you complete the quest
        '''
        self.name = name
        self.description = description
        self.completionStatus = completionStatus
        self.reward = reward

    def printDescription(self):
        '''prints the description of the quest'''
        print(self.name)
        print(self.description)
        if self.completionStatus:
            questStatus = (
                f"\033[38;2;{54};{237};{21}m{'completed'}\033[0m")
        else:
            questStatus = (
                f"\033[38;2;{224};{13};{13}m{'incomplete'}\033[0m")
        print(f"this quest is {questStatus}")