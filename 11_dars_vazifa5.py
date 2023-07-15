# Vazifa
# 5
mahsulotlar = ['olma', 'anor', 'nok', 'un', 'yog\'', 'piyoz', 'uzum', 'tarvuz']
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo\'shing:"))
for mahsulot in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
        a = "bor"
    else:
        mavjud_emas.append(mahsulot)
        a = "yo\'q"
if mavjud_emas:
    print(f"Do\'konimizda quyidagi mahsulotlar yo\'q: {mavjud_emas}")
elif len(mavjud_emas) == 1:
    print(f"do\'konimizda faqatgina {mavjud_emas} yo\'q.")
else:
    print("Siz so\'ragan barcha mahsulotlar do\'konimizda bor.")
