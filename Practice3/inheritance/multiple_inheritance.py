class Walk:
    def move(self):
        return "Walking"

class Fly:
    def fly(self):
        return "Flying"

class Bird(Walk, Fly):
    pass

b = Bird()
print(b.move())
print(b.fly())
