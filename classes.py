class Char:

    def __init__(self, name, health, damage, defense, energy):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defense
        self.energy = energy


class Mage(Char):

    className = "Binary Mage"
    base_health = 75
    base_damage = 30
    base_defense = 40
    base_energy = 120

    def __init__(self, name):
        Char.__init__(self, name, self.base_health, self.base_damage, self.base_defense, self.base_energy)
        self.color = "yellow"


class Warrior(Char):

    className = "Encryption Warrior"
    base_health = 120
    base_damage = 15
    base_defense = 70
    base_energy = 50

    def __init__(self, name):
        Char.__init__(self, name, self.base_health, self.base_damage, self.base_defense, self.base_energy)
        self.color = "blue"


class Hunter(Char):

    className = "Algorithm Hunter"
    base_health = 90
    base_damage = 20
    base_defense = 50
    base_energy = 80

    def __init__(self, name):
        Char.__init__(self, name, self.base_health, self.base_damage, self.base_defense, self.base_energy)
        self.color = "magenta"


