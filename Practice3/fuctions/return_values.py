def analyze(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

a, b, c = analyze([5, 8, 2, 10])
print(a, b, c)
