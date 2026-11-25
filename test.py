pairs = [("교통", 1500), ("식비", 24000)]
print(sorted(pairs, key=lambda pair:pair[1], reverse=True))
pair = ("식비", 24000)
print(pairs[0][0])

biggest = None