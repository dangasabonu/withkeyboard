# 13-dars. Dictionary
# Muallif: Maftuna
# Sana: 14.07.2023

# meva = {'tur':'anor', 'tam':'nordon'}
# print(meva['tur'])
# print(meva['tam'])
en_uz = {'dandelion': 'momoqaymoq', 'cow': 'sigir', 'dog': "it"}
idishlar = {"piyola": 5000, "kosa": 8000, "lagan": 15000}
print(f"Piyola narxi {idishlar['piyola']} so'm")
talaba = {'ism': "madina olimova", "yosh": 15, "t_yil": 2008}
print(f"{talaba['ism'].title()},\
{talaba['t_yil']}-yilda tug\'ilgan,\
{talaba['yosh']} yoshda")
talaba["kurs"] = 4
talaba["fakultet"] = "informatika"
talaba['ism'] = 'odina'
# bo'sh lug'at
talaba_1 = {}
# talaba_1["ism"] = input("ismi nima")
del talaba["yosh"]
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'soli': 'mi 10 pro',
    'salim': 'nokia 33110',
    'karim': 'pixel 3xl'
    }
print(telefonlar['ali'])
print(telefonlar['soli'])

# get() metodi
phone = telefonlar.get('hasan', "Bunday ism mavjud emas.")
print(phone)
phone = telefonlar.get('hasan')
print(phone)
meva = en_uz.get('dandelion')
print(meva)
