class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    pass

d = Dog()
print(d.sound())
