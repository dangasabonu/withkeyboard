# Vazifa 07-dars
# 1
ismlar = ['Munavvar', "Odina"]
print("Salom ", ismlar[0], 'Bugun ham kechagidek harakat qilamizmi?')
print(f'Matematika bo\'yicha yordam kerak emasmi {ismlar[1]}?')
# 2
sonlar = [13, 0, -7, 13.12, -23.11, 2300]

# 3
t_shaxslar = ['Amir Temur', 'Muhammad Mustafo', 'Islom Karimov']
z_shaxslar = ["Bill Gates", 'Davronbek Turdiyev', 'Kim Teahyung']

# 4
shaxs1 = 'Islom Karimov'
shaxs2 = 'Kim Teahyung'
# print(f'Men tarixiy shaxslardan {shaxs1} bilan, ')
# print(f'zamonaviy shaxslardan esa {shaxs2} bilan suhbat qurishni istar edim')

# 5
friends = []
friends.append("Xumoyun")
friends.append("Shaxina")
friends.append("Bobur")
friends.append("Gullola")
friends.append("Munavvar")

# 6
friends.remove("Xumoyun")  # olib tashlash
friends.remove("Shaxina")  # olib tashlash
print(friends)
# 7
friends.insert(0, 'Azizbek')
friends.append("Mahliyo")
friends.insert(1, "Odina")
friends.append("Michael Jackson")
friends.insert(2, "Lily")
friends.insert(2, "Jeon Jungkook")
print(friends)
# 8
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(6))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(4))
mehmonlar.append(friends.pop(2))
print("Kelgan mehmonlar:", mehmonlar)
