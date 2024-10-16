# Abu H Kamal
# Inheritance of Class

class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def describe(self):
        return "the dog says: Woof!"


class Cat(Pet):
    def describe(self):
        return "the cat says: Meow!"


fred = Dog("Fred")
misha = Cat("Misha")
print(fred.name + " " + fred.describe())
print(misha.name + " " + misha.describe())
