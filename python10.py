pairs = [(1, 3), (2, 2), (4, 1)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(4, 1), (2, 2), (1, 3)]
