


class Critter:
    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return self.hitpoints > 0

    def attack(self, target):
        damage = min(self.damage, target.hitpoints)
        target.hitpoints -= damage
        return damage


class Goblin(Critter):
    hitpoints = 10
    damage = 3

    def describe(self):
        return "Goby the Goblin"


class Orc(Critter):
    hitpoints = 15
    damage = 5

    def describe(self):
        return "Morgash the Orc"

goby = Goblin('Goby')
print(goby.name)
print(goby.hitpoints)
print(goby.damage)

morgash = Orc('Morgash')
print(morgash.name)
print(morgash.hitpoints)
print(morgash.damage)
print(morgash.is_alive())
morgash.hitpoints = 0
print(morgash.is_alive())
morgash.hitpoints = 10
print(morgash.is_alive())
print(isinstance(goby, Critter))
print(isinstance(morgash, Critter))
print(goby.hitpoints)
print(morgash.hitpoints)
print(morgash.attack(goby))
print(goby.hitpoints)
print(goby.attack(morgash))
print(goby.attack(morgash))
print(morgash.hitpoints)
print(goby.attack(morgash))
print(morgash.hitpoints)
print(goby.attack(morgash))
print(morgash.hitpoints)
print(goby.attack(morgash))
print(morgash.hitpoints)
print(goby.describe())
print(morgash.describe())
