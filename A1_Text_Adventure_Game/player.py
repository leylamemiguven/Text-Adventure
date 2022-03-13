
from item import Item, Bandages, Sword, Shield
class Player():

    def __init__(self, name, health, inventory, location):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.location = location
 
    def move(self, user_choice):
        #Moves the player to the user selected option and prints the string representation of the location.
        self.location = user_choice
        self.show_location()

    def pick_item(self, cave_items):
        #Adds items found in the cave to the players' inventory

        for item in cave_items:
            if item.name not in self.inventory:
                self.inventory[item.name] = 1
            elif item.name in self.inventory:
                self.inventory[item.name] += 1
            
        
        print(self.show_inventory())

    def show_inventory(self):
        #returns inventory

        return "Your inventory: {}".format(self.inventory)
        
            
    def heal_self(self):
        #Adds health points to the player's health
        old_health = self.health
        if "Bandage" in self.inventory:
            for i in range(self.inventory["Bandage"]):
                self.health += Bandages(0).heal
            print("With the help of bandages you picked up your health has increased from {} to {}!". format(old_health,self.health))

        elif "Bandage" not in self.inventory:
            print("You can't heal yourself without any bandages!")


    def show_location(self):
        #prints the string representation location of the player in respect to which cave they are located.

        rep_list = ["[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]","[ ]"]

        rep_string = ''

        rep_list[self.location-1] = "[*]"

        n = 4 

        for i, x in enumerate(rep_list):
            if i % n == 0:
                rep_string += " \n"
            rep_string += x
            
        print("You are here: \n {} ".format(rep_string))


