# Vazifa
# 1
ismlar = ["Pushkin", "Navoiy", "Shekspir", "A.P.Chexov"]
for ism in ismlar:
    print(f"Har bir adabiyotshunos {ism} ni taniydi.")
print(f"Kod {len(ismlar)} marta takrorlandi")
# 2
sonlar = list(range(10, 100))
for son in sonlar:
    print(son**3)
# 3
kinolar = []
print("5 ta eng sevimli filmingiz qaysilar?")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-filmingiz nomini kiriting \n>>>"))
print(f"Sizning sevimli kinolaringiz: {kinolar}")

# 4
kishilar = []
n = input("Bugun necha kishi bilan suhbatlashdingiz?\n>>>")
n = int(n)
for a in range(n):
    kishilar.append(input(f"{a+1}-odam kim edi?\n"))
print(kishilar)
