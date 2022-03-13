class Item():
    def __init__(self, name):
        self.name = name


class Bandages(Item):

    def __init__(self, name,):
        super().__init__(name)
        self.name = "Bandage"
        self.heal = 60

     
class Sword(Item): 

    def __init__(self, name):
        super().__init__(name)
        self.name = "Sword"
        self.attack = 50


class Shield(Item):

    def __init__(self, name):
        super().__init__(name)
        self.name = "Shield"
        self.defend = 80


