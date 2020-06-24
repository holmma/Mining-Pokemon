from random import *


class Fight:
    def __init__(self, Pokemon1, Pokemon2):
        self.Pokemon1 = Pokemon1
        self.Pokemon2 = Pokemon2
        self.hp1 = Pokemon1.hp
        self.hp2 = Pokemon2.hp

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
        if(self.Pokemon1.attack > self.Pokemon1.specialAttack):
            self.hp2 = self.hp2-(50 * self.Pokemon1.attack/(
                50 * self.Pokemon2.defense))
        else:
            self.hp2 = self.hp2-(50 * self.Pokemon1.specialAttack/(
                50 * self.Pokemon2.specialDefense))

    def attack2(self):
        if(self.Pokemon2.attack > self.Pokemon2.specialAttack):
            self.hp1 = self.hp1-(50 * self.Pokemon2.attack/(
                50 * self.Pokemon1.defense))
        else:
            self.hp1 = self.hp1-(50 * self.Pokemon2.specialAttack/(
                50 * self.Pokemon1.specialDefense))

    def fight(self):
        i = 1
        while(self.hp1 > 0 and self.hp2 > 0):
            if(i == 1):
                self.attack1()
            else:
                self.attack2()
            i = i+1
            if(i == 3):
                i = 1

        if(self.hp2 <= 0):
            if(self.Pokemon1.score > self.Pokemon2.score):
                s = True
            else:
                s = False
            #return str(s)+'\nPokemon 1 Restliche HP:{}'.format(int(self.hp1)) + "\n"+self.Pokemon1.to_String()
            self.Pokemon1.add_win()
            return s
        if(self.hp1 <= 0):
            if(self.Pokemon1.score < self.Pokemon2.score):
                s = True
            else:
                s = False
            #return str(s)+'\nPokemon 2 Restliche HP:{}'.format(int(self.hp2)) + "\n"+self.Pokemon2.to_String()
            self.Pokemon2.add_win()
            return s

    def fight_ml(self):
        i = 1
        while(self.hp1 > 0 and self.hp2 > 0):
            if(i == 1):
                self.attack1()
            else:
                self.attack2()
            i = i+1
            if(i == 3):
                i = 1

        if(self.hp2 <= 0):
            return {'name1': [self.Pokemon1.name], 'hp1': [self.Pokemon1.hp], 'attack1': [self.Pokemon1.attack], 'defense1': [self.Pokemon1.defense], 'specialAttack1': [self.Pokemon1.specialAttack], 'specialDefense1': [self.Pokemon1.specialDefense], 'speed1': [self.Pokemon1.speed],
                    'name2': [self.Pokemon2.name], 'hp2': [self.Pokemon2.hp], 'attack2': [self.Pokemon2.attack], 'defense2': [self.Pokemon2.defense], 'specialAttack2': [self.Pokemon2.specialAttack], 'specialDefense2': [self.Pokemon2.specialDefense], 'speed2': [self.Pokemon2.speed], 'Gewonnen': True}
        if(self.hp1 <= 0):
            return {'name1': [self.Pokemon1.name], 'hp1': [self.Pokemon1.hp], 'attack1': [self.Pokemon1.attack], 'defense1': [self.Pokemon1.defense], 'specialAttack1': [self.Pokemon1.specialAttack], 'specialDefense1': [self.Pokemon1.specialDefense], 'speed1': [self.Pokemon1.speed],
                    'name2': [self.Pokemon2.name], 'hp2': [self.Pokemon2.hp], 'attack2': [self.Pokemon2.attack], 'defense2': [self.Pokemon2.defense], 'specialAttack2': [self.Pokemon2.specialAttack], 'specialDefense2': [self.Pokemon2.specialDefense], 'speed2': [self.Pokemon2.speed], 'Gewonnen': False}
