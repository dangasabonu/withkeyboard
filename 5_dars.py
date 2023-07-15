# 05-dars. String (Matn)
# Sana: 5/06/2023
# Muallif: Dangasabonu & Munavvar

ism = "Shodiyona"

shahar = "Қўқон"
viloyat = "Фарғона"

matn = "Biz ertaga 🏔 ga ketyapmiz \nMenda 🐈 bor"
smayl = "😍"
smayl_2="🥰"
print(matn)



# STRING USTIDA AMALLAR
ism = "Ra\'no"
print("Uning ismi "+ism)

ism = " So Jun "
familiya = "Xan"
print( familiya + ism)

ism = "Dilshodbek"
familiya = "Usmanov"
print(ism + ' ' + familiya )



# f-string
ism = 'Lola'
familiya = 'Aliyeva'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)

ism = "Alisher"
familiya = "Abdug\'aniyev"
print(f"Salom, mening ismim {ism}. {ism} {familiya}")



# MAXSUS BELGILAR
print('Hello World!')
print('Hello \tWorld!')
print('Hello \nWorld!')



# STRING METODLAR 
ism = "jobir"
familiya = "yuldoshboyev"
ism_sharif = f'{ism} {familiya}'
print(ism_sharif.upper())
ism_sharif = ism_sharif.upper()
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())

poyabzal = '    tufli    '
print('Men kecha',poyabzal.lstrip(), 'sotib oldim.')
print('Men kecha',poyabzal.rstrip(), 'sotib oldim.')
print('Men kecha',poyabzal.strip(), 'sotib oldim.')



#INPUT
ism = input('Ismingiz nima?\n>>>') #foydalanuvchidan ismini so'rash
print('Assalomu alaykum ',ism.title()) 








