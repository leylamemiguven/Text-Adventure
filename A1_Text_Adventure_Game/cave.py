
class Cave():

    def __init__(self, name, enemies, items, location):
        self.name = name
        self.enemies = enemies
        self.items = items
        self.location = location 

    def __str__(self):
    #Prints off the enemies and items present in the cave. For example, 
    # "You entered a cave with 2 Tribesman and 1 Sabertooth Tigers. 
 

        if len(self.enemies) >=1:

            enemies_in_cave = {}
            for enemy in self.enemies:
                # print(enemy.__str__())
                if enemy.name in enemies_in_cave:
                    enemies_in_cave[enemy.name] += 1
                elif enemy.name not in enemies_in_cave:
                    enemies_in_cave[enemy.name] = 1
            # print(enemies_in_cave)


            s = ''
            n = 0
            extra = ''

            new = enemies_in_cave.copy()
            
            for e in enemies_in_cave:
                if len(enemies_in_cave) > 1 and n!= len(enemies_in_cave):
                    n += 1
                    if n>1:
                        s += "and "

                if enemies_in_cave[e] > 1:
                    extra += e + "s"
                elif enemies_in_cave[e] == 1:
                    extra = e
                s += "{} {} ".format(str(enemies_in_cave[e]), extra)
                
        
        
            return "You entered {} with {} ".format(self.name, s)

        elif self.enemies == []:
            return "There are no enemies present in {} ".format(self.name)
    
    def show_items(self):


        if len(self.items) >= 1:
            items_in_cave = {}
            for item in self.items:
                # print(item)
                if item.name in items_in_cave:
                    items_in_cave[item.name] += 1
                elif item.name not in items_in_cave:
                    items_in_cave[item.name] = 1
            # print(items_in_cave)

            s = ''
            n = 0
            extra = ''

            new = items_in_cave.copy()
            
            for i in items_in_cave:
                if len(items_in_cave) > 1 and n!= len(items_in_cave):
                    n += 1
                    if n>1:
                        s += "and "

                if items_in_cave[i] > 1:
                    extra += i + "s"
                elif items_in_cave[i] == 1:
                    extra = i
                s += "{} {} ".format(str(items_in_cave[i]), extra)
            return "Items found in {}: {} ".format(self.name, s)

        elif len(self.items) == 0:
            return "There are no items present in {} ".format(self.name)
    
