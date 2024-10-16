



class Pet:
    sound = ''
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.sound + '!'
    def describe(self):
        kind_of_pet = self.__class__.__name__.lower()
        return f' the {kind_of_pet} says: {self.speak()}!'

class Dog(Pet):   # take name of super class, inheritance relation

    sound = "Woof"

class LapDog(Dog):

    sound = "Yip"

class LoudLapDog(LapDog):
    def speak(self):
        return super().speak().upper() * 3

