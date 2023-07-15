# 10-dars. Tarmoqlanish
mevalar = ['kivi', 'apelsin', 'guava', 'avakado']
mevalar.append("handalak")
for meva in mevalar:
    print(meva.title())
for meva in mevalar:
    if meva == "handalak":  # bunda "=="-tengmi degan manoda ishlatilgan
        print(meva.upper())
    else:
        print(meva.title())
ism = input('Ismingiz nima? \n>>>')
if ism.lower() != "lola":
    print(f"Uzr, {ism.title()} biz Lolani kutyapmiz. ")
else:
    print("Salom Lola")
javob = float(input("13x13 nechchiga teng?\n>>> "))
if javob != 169:
    print("Javob xato!")
yosh = int(input("Yoshingiz nechida?\n>>>  "))
if yosh >= 18:
    print("Xush kelibsiz!")
else:
    print("Kirish mumkin emas!")
parol = input("Yangi parol tanlang:\n")
if len(parol) <= 8:
    print("Parol 8 ta belgidan ko\'p bo\'lishi kerak!")
else:
    print("Parol muvaffaqiyatli o\'rnatildi.")
yil = int(input("Tug\'ilgan yilingizni kiriting: \n>>>"))
if 2023-yil < 16:
    print(f"Siz {2023-yosh} yoshda ekansiz.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz!")
yosh = int(input("Yoshingiz nechida?\n "))
if yosh > 12:
    print("Siz 12 yoshdan kattasiz.")
