5/29/2024
- created change log
- created basic dev work
- started work on basic lootboxes
- created basic shop function

5/30/2024
- created lootbox class
    - lootTable attribute
    - counter attribute
    - roll method
    - counter method

5/31/2024
- added colored text
- added aligned text
- started work on player class
    - printInv method
    - inventory attribute

6/3/2024
- Player changes:
    - added coins attribute to the player
- Lootbox changes:
    - Lootbox class takes Inventory parameter
        - stores obtained items in the player's inventory
    - BasicLootbox subclass of lootbox
        - made this so that I can use \_\_str\_\_() method
- Misc changes:
    - moved text colors to main
        - modified classes to take textColour parameter
    - buying lootboxes now costs coins
    - improved shop menu

6/4/2024
- Lootbox cost now works
- Started work on quests
    - just gives you gold for now

6/5/2024
- Made a main menu
    - Made a movement menu
- Made a guild menu where you go to accept quests
- Added acceptedQuests attribute to player
- more work on quests

6/5/2024
- Removed BasicLootbox subclass
- Added name attribute to Lootbox class
- -Added Quests class
    - name attribute
    - description attribute
    - completionStatus attribute
    - reward attribute