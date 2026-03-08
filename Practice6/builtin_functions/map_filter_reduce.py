from functools import reduce

f = open("sample.txt", "r")
lines = f.readlines()
f.close()

scores = []

for line in lines:
    name, score = line.split()
    scores.append(int(score))

# map
double = list(map(lambda x: x*2, scores))
print(double)

# filter
high = list(filter(lambda x: x > 85, scores))
print(high)

# reduce
total = reduce(lambda a,b: a+b, scores)
print(total)