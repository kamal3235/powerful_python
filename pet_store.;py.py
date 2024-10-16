# inheritance
# avoid repeatation
# super class or base class
# dont need constructor for subclass
# isinstance() is built-in, find an object is an instance
# of class or not
# an object is an instance of its class and
# also instance of all super class
# Magic attribute __class__ and __name__
# Every subclass can use


class Pet:
    def __init__(self, name):
        self.name = name
    def describe(self):
        kind_of_pet = self.__class__.__name__.lower()
        return f' the {kind_of_pet} says: {self.sound}!'

class Dog(Pet):   # take name of super class, inheritance relation
    # def __init__(self, name):
    #     self.name = name
    # def describe(self):
    #     return "the dog says: woof!"
    sound = "Woof"

class LapDog(Dog):
    # def describe(self):
    #     return "the lap dog says: Yip!"
    sound = "Yip"

class LoudLapDog(LapDog):
    # def describe(self):
    #     return "the loud lap dog says: YIP!"
    sound = "YIP"

class Bird(Pet):
    # def __init__(self, name):
    #     self.name = name

    # def describe(self):
    #     return "the bird says: Chirp!"
    sound = "Chirp"

class Cat(Pet):
    # def __init__(self, name):
    #     self.name = name

    # def describe(self):
    #     return "the cat says: Meow!"
    sound = "Meow"


fido = Dog("Fido")
print(fido.describe())
buck = Dog('Buck')
print(buck.describe())
shorty = LapDog('Shorty')
print()
biff = LapDog('Biff')
print(isinstance(biff, LapDog))
print(isinstance(biff, LoudLapDog))
print(isinstance(biff, Dog))
print(isinstance(biff, Pet))
print()
print(shorty.describe())
pip = LoudLapDog("Pip")
print(pip.describe())
print()
fluffy = Cat('Fluffy')
print(fluffy.describe())
print()
rover = Dog('Rover')
print(rover.describe())
misty = Cat('Misty')
print(misty.describe())
angel = Bird('Angel')
print(angel.describe())
