f = open("sample.txt", "r")
lines = f.readlines()
f.close()

names = []
scores = []

for line in lines:
    name, score = line.split()
    names.append(name)
    scores.append(int(score))

# enumerate
for i, name in enumerate(names):
    print(i, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

print(len(scores))
print(sum(scores))
print(min(scores))
print(max(scores))
print(sorted(scores))

x = "100"
y = int(x)
print(type(y))