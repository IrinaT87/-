class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name=name
        self.power=power
        self.energy=energy
        self.hands=hands
        # self.backpack=[]

    def eat(self, food):
        if self.energy < 100:
            self.energy+=food
        else:
            print('Not hungry')


    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy-=hours*2
            self.power+=hours*2
        else:
            print('Too tired')


    def change_alias(self, new_alias):
        self.alias=new_alias


    def beat_up(self, foe):
        if not isinstance (foe,Character):
            return
        if foe.power<self.power:
            foe.status='defeated'
            self.status='winner'
        else:
            print('Retreat!')

    def move(self):
        print('Moving on 2 square')

    def attack(self,foe):
        foe.health-=10

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power=power
        self.energy=energy
        self.hands=hands

    def webshoot(self):
        print('Pew-Pew!')

    def move(self):
        self.webshoots()
        print('Moving on 1 square')

    def attack(self,foe):
        foe.status='Stunned'


class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack=[]

    def turn_spider_sense(self):
        self.energy-=10
        self.power+=20

    def move(self):
        self.webshoots()
        print('Moving on 3 square')

    def webshoot(self):
        if 'Web' in self.backpack:
            super().webshoot()
        else:
            print('No web!')

    def attack(self, foe):
        super().attack(foe)
        Spider.attack(self, foe)

    def __lt__(self, other):
        if not isinstance (other, Character):
            print('Not a Character!')
            return
        return self.power < other.power

    

peter_parker=SpiderMan('Peter Parker', 80)
miles_morales=SpiderMan('Miles Morales', 85)
print(peter_parker.__lt__(miles_morales))
# enemy=Character('Some Enemy', 10)
# enemy.health=100
# peter_parker.attack(enemy)

# print(enemy.health)
# print(enemy.status)
# # peter_parker.move()

# peter_parker.backpack.append('Web')
# peter_parker.webshoot()

# peter=Character('Peter Parker', 80)
# peter.alias='Spider-man'   
# peter.backpack.append('web-shooters')
 
# bruce=Character('Bruce Wayne', 85)
# bruce.alias='Batman'

# bruce.beat_up(peter)
# print(peter.status)
# print(bruce.status)
