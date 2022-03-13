
class Enemy():
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
    def __str__(self) -> str:
        #prints out the enemy
        return "a {}".format(self.name)

class Tribesman(Enemy):

    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.name = "Tribesman"
        self.attack_power = 10


class Saberthooth_Tiger(Enemy):

    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.name = "Sabertooth Tiger"
        self.attack_power = 20


class War_Maiden(Enemy):

    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.name = "War-Maiden"
        self.attack_power = 50


class Ice_Serpent(Enemy):

    def __init__(self, name, attack_power):
        super().__init__(name, attack_power)
        self.name = "Ice-Serpent"
        self.attack_power = 90



