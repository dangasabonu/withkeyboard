# Vazifa
# 4
mahsulotlar = ['olma', 'anor', 'nok', 'gilos', 'behi', 'kivi', 'uzum', 'behi']
savat = []
for n in range(5):
    savat.append(input(f'{n+1}- mahsulotni kiriting: '))


for mahsulot in savat:
    if mahsulot.lower() not in mahsulotlar:
        print(f"Do\'konimizda {mahsulot} yo\'q.")
    else:
        print(f"Do\'konimizda {mahsulot} bor.")
