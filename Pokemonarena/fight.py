from random import *


class Fight:
    def __init__(self, Pokemon1, Pokemon2):
        self.Pokemon1 = Pokemon1
        self.Pokemon2 = Pokemon2
        if(Pokemon1.speed > Pokemon2.speed):
            self.start = 1
        elif(Pokemon1.speed == Pokemon2.speed):
            if(randint(1, 2) == 1):
                self.start = 1
            else:
                self.start = 2
        else:
            self.start = 2

    def attack1(self):
        self.Pokemon2.hp = self.Pokemon2.hp-(50 *
                                             self.Pokemon1.attack/(self.Pokemon2.defense))

    def attack2(self):
        self.Pokemon1.hp = self.Pokemon1.hp-(50 *
                                             self.Pokemon2.attack/(self.Pokemon1.defense))

    def fight(self):
        i = 1
        while(self.Pokemon1.hp > 0 and self.Pokemon2.hp > 0):
            if(i == 1):
                self.attack1()
            else:
                self.attack2()
            i = i+1
            if(i == 3):
                i = 1

        if(self.Pokemon1.hp <= 0, ):
            return self.Pokemon1.to_String()
        else:
            return self.Pokemon2.to_String()
