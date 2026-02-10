def make_power(exponent):
    def power(number):
        return number ** exponent
    return power

square = make_power(2)
cube = make_power(3)

print(square(4))
print(cube(2))
