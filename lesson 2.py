class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_enemy(self, enemy):
        enemy.hp -= self.attack
        print(f'Артур бьёт Мерлина на {self.attack}. У Мерлина осталось {enemy.hp} HP')

    def heal(self, amount):
        amount.hp += amount
        if amount.hp > 100:
            amount.hp = 100
    def is_alive(self):
        if self.hp > 0:
            return self.hp

arthur = Hero("Артур", 100, 15)
merlin = Hero("Мерлин", 80, 25)

arthur.attack_enemy(merlin)     # 80 → 65
merlin.attack_enemy(arthur)     # 100 → 75
arthur.heal(50)                 # 75 → 100 (обрезалось, было бы 125)
arthur.heal(10)                 # остаётся 100
print(arthur.is_alive())        # True
print(merlin.is_alive())        # True



