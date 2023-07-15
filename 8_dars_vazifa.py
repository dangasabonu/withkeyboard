# Vazifa
# 1

davlatlar = ["Vetnam", "Gvineya", "Togo", "Kambodja", "Ruanda"]
print(davlatlar)

# 2
print(len(davlatlar))

# 3
print(sorted(davlatlar))

# 4
print(sorted(davlatlar, reverse=True))

# 5
print(davlatlar)

# 6
davlatlar.reverse()
print(davlatlar)

# 7
davlatlar.sort()
davlatlar.sort(reverse=True)

# 8
sonlar = list(range(120, 1200, 2))

# 9
print(sum(sonlar))

# 10
print(max(sonlar)-min(sonlar))

# 11
print(len(sonlar))

# 12
print(sonlar[0:20])
print(sonlar[160:180])
print(sonlar[-20:])

# 13
taomlar = ["norin", "turducken", "ramyon", "laddu", "ratatuy"]

# 14
nonushta = taomlar[:]
del nonushta[0]
del nonushta[1]
nonushta.append("quymoq")
nonushta.append("pealle")

# 15
print(nonushta)
print(taomlar)

# 16
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"
