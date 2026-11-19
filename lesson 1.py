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


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

voina_and_mir = Book('Война и мир', "Лев Николаевьич Толстой", 1730)
master_and_margaritte = Book("Мастер и маргарита", "Булгаков", 480)

print(voina_and_mir.title, voina_and_mir.author, voina_and_mir.pages)
print(master_and_margaritte.title, master_and_margaritte.author, master_and_margaritte.pages)


