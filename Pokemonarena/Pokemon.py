# Pokemon
class Pokemon:

    # Konstruktor
    def __init__(self, name, hp, attack, defense, specialAttack, specialDefense, speed, score=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.score = score
        self.wins = 0

    def add_win(self):
        self.wins = self.wins+1

    def to_String(self):
        return 'name = {}, hp = {}, attack = {}, defense = {},specialAttack = {}, specialDefense = {}, speed = {}, score = {}'.format(self.name, self.hp, self.attack,
                                                                                                                                      self.defense, self.specialAttack, self.specialDefense, self.speed, self.score)
