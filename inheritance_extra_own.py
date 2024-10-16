class Creature:
    name: str
    hitpoints: int
    damage: int
    armor: int

    def __init__(self, name):
        self.name = name

    def is_alive(self):
        return self.hitpoints > 0

    def select_target(self, enemies):
        return enemies[0]

    def attack(self, target):   # attack method return the net damage done
        damage = self.damage - target.armor

        if damage < 0:
            damage = 0
        target.hitpoints -= damage
        return damage

    def describe(self):
        return f'{self.name} the {self.__class__.__name__}'

class Goblin(Creature):  #goby
    hitpoints = 10
    damage = 3
    armor = 1


    def attack(self, target):
        if isinstance(target, Orc):
            damage = self.damage * 2
        else:
            damage = self.damage
        damage -= target.armor
        if damage < 0:
            damage = 0
        target.hitpoints -= damage
        return damage



class Orc(Creature):   # morgash
    hitpoints = 15
    damage = 5
    armor = 2

    def select_target(self, enemies):
        candidates = [
            enemy for enemy in enemies
            if not isinstance(enemy, Orc)
        ]

        if len(candidates) == 0:
            candidates = enemies
        target = candidates[0]
        for choice in candidates[1:]:
            if choice.armor < target.armor:
                target = choice
        return target


class HillOrc(Orc):   # narbul   why it is subclass of Orc according to  what ????? solution GOT IT 137
    hitpoints = 20
    damage = 5
    armor = 3


    def attack(self, target):
        if isinstance(target, Skeleton):
            damage = 0
        else:
            damage = self.damage
        damage -= target.armor
        if damage < 0:
            damage = 0
        target.hitpoints -= damage
        return damage

class Skeleton(Creature):   # bonez
    hitpoints = 8
    damage = 4
    armor = 0
    def select_target(self, enemies):
        target = enemies[0]
        for choice in enemies[1:]:
            if choice.hitpoints < target.hitpoints:
                target = choice
        return target


class Ewok(Creature):   #teebo
    hitpoints = 4
    damage = 10
    armor = 1


goby = Goblin('Goby')
print(goby.name)    # Goby
print(goby.hitpoints)    #10
print(goby.damage)
print(goby.armor)
morgash = Orc('Morgash')
print(morgash.name)
print(morgash.hitpoints)
print(morgash.damage)
print(morgash.armor)
narbul = HillOrc('Narbul')
print(narbul.name)
print(narbul.hitpoints)
print(narbul.damage)
print(narbul.armor)
bonez = Skeleton('Bonez')
print(bonez.name)
print(bonez.hitpoints)
print(bonez.damage)
print(bonez.armor)
teebo = Ewok('Teebo')
print(teebo.name)
print(teebo.hitpoints)
print(teebo.damage)
print(teebo.armor)
print(isinstance(goby, Creature))
print(isinstance(morgash, Creature))
print(isinstance(narbul, Creature))
print(isinstance(bonez, Creature))
print(isinstance(teebo, Creature))
print(bonez.is_alive())
bonez.hitpoints = 0
print(bonez.is_alive())
bonez.hitpoints = 8
print(bonez.is_alive())
print(goby.hitpoints)
print(bonez.hitpoints)
print(bonez.attack(goby))
print(goby.hitpoints)
print()
print(goby.attack(bonez))
print(bonez.hitpoints)
creatures = [narbul, goby, teebo, bonez, morgash]
target = goby.select_target(creatures)
print(target.name)
target = teebo.select_target(creatures)
print(target.name)
target = bonez.select_target(creatures)
print(target.name)
target = narbul.select_target(creatures)
print(target.name)    # Narbul but unit test showing Bonez ?????????????????????
target = morgash.select_target(creatures)
print(target.name)
only_orcs = [narbul, morgash]
nashba = Orc('Nashba')
target = nashba.select_target(only_orcs)
print(target.name)
print(bonez.hitpoints)
print(narbul.attack(bonez))
print(narbul.attack(bonez))
print(narbul.attack(bonez))
print(bonez.hitpoints)
print(nashba.hitpoints)
print(goby.attack(nashba))
print(nashba.hitpoints)
print(narbul.hitpoints)
print(goby.attack(narbul))
print(narbul.hitpoints)
