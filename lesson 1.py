class Hero:
    def __init__(self, name, hp = 100, attack = 10):
        self.name = name
        self.hp = hp
        self.attack = attack



artur = Hero('Артур', attack=15)
merlin = Hero('Мерлин', 80, 25)
lancelot = Hero('Ланселот')

print(artur.name, artur.hp, artur.attack, '\n',
      merlin.name, merlin.hp, merlin.attack, '\n',
      lancelot.name, lancelot.hp, lancelot.attack)