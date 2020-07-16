# Pokemon
class Pokemon:

    # Konstruktor
    def __init__(self, name, hp, attack, defense, specialAttack, specialDefense, speed, score=0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.score = score
        self.wins = 0
        self.averageScore = 0
<<<<<<< HEAD


=======
>>>>>>> dbb5abb99fee71193df9331d381ad7580c16bb38

    def add_win(self):
        self.wins = self.wins+1

    def to_String(self):
        return 'name = {}, hp = {}, attack = {}, defense = {},specialAttack = {}, specialDefense = {}, speed = {}, score = {}'.format(self.name, self.hp, self.attack,
                                                                                                                                      self.defense, self.specialAttack, self.specialDefense, self.speed, self.score)

    def to_df_dict(self):
        return {'name': [self.name], 'hp': [self.hp], 'attack': [self.attack], 'defense': [self.defense], 'specialAttack': [self.specialAttack], 'specialDefense': [self.specialDefense], 'speed': [self.speed]}
