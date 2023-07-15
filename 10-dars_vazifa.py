# Vazifa
# 1
import math
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

# 2
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())

# 3
login = input("Loginni kiriting:\n>>> ")
if login.lower() == "admin":
    print(f'Xush kelibsiz {login.title()}. Users ro\'yxatini ko\'rasizmi?')
else:
    print(f"Xush kelibsiz {login.title()}!")

# 4
print("Ikkita son kiriting.")
a = int(input("Birinchi sonni kiriting:\n "))
b = int(input("Ikkinchi sonni kiriting:\n "))
if a == b:
    print(f"{a}, {b} ga teng. Sonlar teng ekan.")

# 5
son = int(input('Istalgan sonni kiriting:\n '))
if son < 0:
    print("Manfiy son.")
else:
    print("Musbat son")

# 6
num = int(input("Son kiriting:\n "))
if num > 0:
    print(math.sqrt(num))
else:
    print("Musbat son kiriting")
