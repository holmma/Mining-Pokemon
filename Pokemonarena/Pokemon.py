# Pokemon
class Pokemon:

    # Konstruktor
    def __init__(self, name, hp, attack, defense, specialAttack, specialDefense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.specialAttack = specialAttack
        self.specialDefense = specialDefense
        self.speed = speed
        self.score = None