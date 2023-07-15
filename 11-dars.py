# 11-dars. If Elif Else
# yosh = int(input("Yoshingiz nechida?\n "))
# if yosh <= 4:
#     narh = 0
# elif yosh <= 12:
#     narh = 5000
# elif yosh <= 18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so\'m")
# dars = input("Bundan keyin qaysi dars?\n")
# if dars.lower() == "ona tili" or dars.lower() == "kimyo":
#     print("Qochdik darsdan😆")
# else:
#     print("Darsga kettik.")
# kun = input("Bugun nima kun? ")
# havo = float(input("Havo harorati qanday? "))
# if kun.lower() == "yakshanba" or havo >= 30:
#     print("Cho\'milgani ketdik.")
# elif kun.lower() == "yakshanba" or havo >= 30:
#     print("Uyda dam olamiz.")
# else:
#     print("2+2=?(я не робот)")
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000
# print(f"Jami {narx} so\'m")
# narx = 20000
# choy = True
# salat = True
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi.")
#     narx = narx + 1000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 3000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx + 2000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx = narx + 5000
# print(f"Jami {narx} so\'m bo\'ldi")
# ovqat = input("Nima ovqat yeysiz?\n>>> ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Afsuski bizda bunday ovqat yo\'q.")
menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
if buyurtmalar:
    print(f"Ro'yxatda {len(buyurtmalar)} ta taom bor.")

    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor.")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Ro\'yxat bo\'sh.")