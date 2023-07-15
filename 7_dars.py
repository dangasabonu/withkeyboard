# 06-dars Sonlar
# sana: 06/06/2023
# Muallif: Dangasabonu & Munavvar

# Ro'yxat yaratish
# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik']  # matnli
# narxlar = [12000, 18000, 10900, 22000, 25000, 36000]  # sonlar qatnashgan
# sonlar = ['bir', 'ikki', 3, 4, 5]  # aralash ro'yxat
# ismlar = []  # bo'sh ro'yxat

# Ro'yxatga elementlar qo'shish
# append() metodi elementni ro' yxat oxiriga qo'shadi
# mevalar.append('tarvuz')
# print(mevalar)
# insert(indeks,'element') bu metod elementni biz kiritgan indeksga qo'shadi
# del mevalar[0]
# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
mahsulot = bozorlik.pop(1)
print("Men ", mahsulot, "sotib oldim.")
print("Olinmagan mahsulotlar: ", bozorlik)
mahsulot2 = bozorlik.pop()
print(bozorlik)

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]  # mevalar ro'yxati (matnlar)
narhlar = [12000, 18000, 10900, 22000]  # narhlar ro'yxati (sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5]  # sonlar va matnlar aralash ro'yxat
ismlar = []  # bo'sh ro'yxat

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]  # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
