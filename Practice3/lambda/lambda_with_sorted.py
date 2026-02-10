data = [
    {"name": "Dais", "score": 88},
    {"name": "Noni", "score": 95},
    {"name": "Eldar", "score": 88}
]

sorted_data = sorted(data, key=lambda x: (-x["score"], x["name"]))
print(sorted_data)
