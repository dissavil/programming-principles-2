numbers = list(range(1, 30))
result = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))
print(result)
