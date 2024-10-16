# all class has magic attribute

class Quarter:
    def __init__(self):
        self.value = 25
    def in_nickle(self):
        return self.value // 5

class Penny:
    value = 1

coin = Quarter()
another_coin = Quarter()
print(coin.value)
print(another_coin.value)
print(coin.in_nickle())

coin = Penny()
print(coin.__class__)
new_coin = coin.__class__()
print(type(new_coin))