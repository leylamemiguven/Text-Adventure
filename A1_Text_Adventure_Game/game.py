
from player import Player
from enemy import Tribesman, Saberthooth_Tiger, War_Maiden, Ice_Serpent
from item import Bandages, Sword, Shield
from cave import Cave  


class Game():

    def __init__(self, player, caves) -> None:
        self.player = player
        self.caves = caves


    def move_aroud_game(self):
        #Makes the player move arounf the game world according to the player's choices

        move_input = input("Where would you like to move? \nEnter U for UP, D for DOWN, R for RIGHT, L for LEFT. Bare in mind that movement it limited to some directions in various caves: ")
        print(move_input)

        if move_input  == "R" or move_input  == "r":
            if self.player.location == 1 or self.player.location == 2 or self.player.location == 3 or self.player.location == 5 or self.player.location == 6 or self.player.location == 7 or self.player.location == 9 or self.player.location == 10 or self.player.location == 11 or self.player.location == 13 or self.player.location == 14 or self.player.location == 15 :
                p.move(self.player.location + 1)

            else:
                print("You can't move in this direction!")

        elif move_input  == "L" or move_input  == "l":
            if self.player.location == 2 or self.player.location == 3 or self.player.location == 4 or self.player.location == 6 or self.player.location == 7 or self.player.location == 8 or self.player.location == 10 or self.player.location == 11 or self.player.location == 12 or self.player.location == 14 or self.player.location == 15 or self.player.location == 16 :
                p.move(self.player.location - 1)

            else:
                print("You can't move in this direction!")

        elif move_input  == "U" or move_input  == "u":
            if self.player.location == 5 or self.player.location == 6 or self.player.location == 7 or self.player.location == 8 or self.player.location == 9 or self.player.location == 10 or self.player.location == 11 or self.player.location == 12 or self.player.location == 13 or self.player.location == 14 or self.player.location == 15 or self.player.location == 16 :
                p.move(self.player.location - 4)

            else:
                print("You can't move in this direction!")

        elif move_input  == "D" or move_input  == "d":
            if self.player.location == 1 or self.player.location == 2 or self.player.location == 3 or self.player.location == 4 or self.player.location == 5 or self.player.location == 6 or self.player.location == 7 or self.player.location == 8 or self.player.location == 9 or self.player.location == 10 or self.player.location == 11 or self.player.location == 12 :
                    p.move(self.player.location + 4)

            else:
                print("You can't move in this direction!")

        else:
            print("Please enter a viable direction, R, L, U or D")

        if self.player.location == 16:
            game_status = "finished"
            print("CONGRATULATIONS! You managed to find the escape tunnel and escaped!")
            return game_status
           
    def prompt_pick_up(self):
        #Prompts player to pick up an item when there are no enemies in the cave.

        pick_up_confirmation = input("Would you like to pick up items found in the cave? Please type Y for YES or N FOR NO ")
        if pick_up_confirmation == "Y" or pick_up_confirmation == "y":
            self.player.pick_item(cave.items)
            cave.items = {}

        elif pick_up_confirmation == "N" or pick_up_confirmation == "n":
            print("You have decided not to pick up any items")

        elif pick_up_confirmation != "N" or pick_up_confirmation != "n" or pick_up_confirmation != "Y" or pick_up_confirmation != "y":
            print("Please type a viable answer, Y for YES or N for NO ")

    def prompt_heal(self):
        #Makes the player heal themselves when they pick up bandages
        self.player.heal_self()

    def prompt_attack_or_defend(self) -> str:
        #Prompts player to attack, defend or both dependign on what weapon they have in their inventory. 
        # With a sword they are able to kill enemies and with a shield they are able to fend off attacks

        if len(cave.enemies) >= 1:
            old_health = p.health
            enemy_damage = 0
            if "Shield" not in p.inventory:
                for enemy in cave.enemies:
                    enemy_damage += enemy.attack_power
                p.health -= enemy_damage
                if p.health <= 0:
                    player_status = "dead"
                    print("Enemies attacked you and you didn't have enough health! You died :(")
                    return player_status
                elif p.health>= 0:
            
                    print("Enemies have attacked you and lowered your health from {} to {}. \nBetter pick up a shield  when you find it so you can fend off attacks next time".format(old_health, p.health))
            
            elif "Shield" in p.inventory:
                print("Enemies tries attacking you, but you protected yourself with your shield!")
                
            if "Sword" in p.inventory:

                while len(cave.enemies) != 0:
                    for enemy in cave.enemies:
                        print("You killed the {}".format(enemy.name))
                        cave.enemies.remove(enemy)

                print("{}any longer as you defeated them.".format(cave.__str__()))


#Creating Game Objects Here
                
#build all the enemies here

t1 = Tribesman(0, 0)
t2 = Tribesman(0, 0)
t3 = Tribesman(0, 0)
t4 = Tribesman(0, 0)
t5 = Tribesman(0, 0)
t6 = Tribesman(0, 0)
t7 = Tribesman(0, 0)
t8 = Tribesman(0, 0)
t9 = Tribesman(0, 0)
t10 = Tribesman(0, 0)

st1 = Saberthooth_Tiger(0, 0)
st2 = Saberthooth_Tiger(0, 0)
st3 = Saberthooth_Tiger(0, 0)
st4 = Saberthooth_Tiger(0, 0)
st5 = Saberthooth_Tiger(0, 0)

wm1 = War_Maiden(0, 0)
wm2 = War_Maiden(0, 0)
wm3 = War_Maiden(0, 0)
wm4 = War_Maiden(0, 0)
wm5 = War_Maiden(0, 0)
wm6 = War_Maiden(0, 0)


ics1 = Ice_Serpent(0, 0)
ics2 = Ice_Serpent(0, 0)

#build all the items here
b1 = Bandages(0)
b2 = Bandages(0)
b3 = Bandages(0)
b4 = Bandages(0)
b5 = Bandages(0)
b6 = Bandages(0)
b7 = Bandages(0)
b8 = Bandages(0)

sw1 = Sword(0)
sw2 = Sword(0)
sw3 = Sword(0)

sh1 = Shield(0)
sh2 = Shield(0)

#build all the caves here

#Enterance cave
c1 = Cave("Cave 1", [], [], 1)

#middle caves
c2 = Cave("Cave 2", [t1,t2], [b1,b2],2)
c3 = Cave("Cave 3",[],[sh1],3)
c4 = Cave("Cave 4",[wm1],[],4)
c5 = Cave("Cave 5",[],[sw1],5)
c6 = Cave("Cave 6",[st1,t3],[],6)
c7 = Cave("Cave 7",[],[b3,b4,b5,sw1],7)
c8 = Cave("Cave 8",[ics1],[b6],8)
c9 = Cave("Cave 9", [wm2],[sh2],9)
c10 = Cave("Cave 10", [st2,st3,wm3],[],10)
c11 = Cave("Cave 11", [wm4],[],11)
c12 = Cave("Cave 12", [t4,t5,t6], [sw3], 12)
c13 = Cave("Cave 12", [], [b7], 13)
c14 = Cave("Cave 12", [wm5,wm6], [b8], 14)
c15 = Cave("Cave 12", [t4,ics2], [], 15)


#Exit cave
c16 = Cave("Cave 12", [], [], 16)


mountain_caves = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16]



p = Player('Princess', 100, {}, 1)
g = Game(p, mountain_caves)


print("Welcome to ESCAPING PRINCESS! You are an imperial princess kidnapped by one of the mountain tribes. \nYour only chance to escape is to navigate your way through the maze of tunnels and find the exit cave.\nMake sure to pick up items so you can battle enemies that come your way and protect yourself before you reach the exit. \nThough bare in mind you won't be able to pick up items if you haven't defeated all the enemies within the cave first \nThe game will exit if you die OR if you can manage to get to to the exit cave")
(p.show_location())


 

while g.player.health > 0: 

    if g.move_aroud_game() == "finished":
        break


    for cave in mountain_caves:


        if cave.location == g.player.location:
            print(cave.__str__()) 
            print(cave.show_items())



            #Prompts player to pick up items in the cave (prompt pick up item)
            if len(cave.enemies) == 0:
                if len(cave.items) >= 1:
                    g.prompt_pick_up()
                    if "Bandage" in g.player.inventory:
                        g.prompt_heal()
                
            
            elif len(cave.enemies) >= 1:
                if g.prompt_attack_or_defend() == "dead":
                    break



        


            
                
            