# 09-dars For tsikli.
# mehmonlar = ["Ali", "Vali", "Soli", "Hasan", "Husan"]
# print("Salom", mehmonlar[0])
# print("Salom", mehmonlar[1])
# for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, sizni shanba kuni xasharga taklif qilamiz")
# print(f"Hurmat bilan Palonchi sinf\n")
# sonlar = list(range(1, 101))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
# sonlar = list(range(15))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar_kvadrati)
# print(sonlar)
mevalar = []
print("10ta yoqtirmagan mahsulotingizni sanang")
for n in range(10):
    mevalar.append(input(f"{n+1}-mahsulotni kiriting: \n>>>"))
print(f"Siz uchun taomga {mevalar}dan birortasini ishlatmayman.")
