class Game:
    genre = "RPG"

    def __init__(self, title):
        self.title = title

g1 = Game("Skyrim")
g2 = Game("Witcher")

print(g1.genre)
print(g2.title)
