# Vazifa
# 2
yosh = int(input("Yoshingiz nechida?\n "))
if yosh <= 4 or yosh >= 60:
    narx = 0
elif yosh <= 18:
    narx = 10000
else:
    narx = 20000
print(f"Siz uchun muzeyga kirish {narx} so\'m.")
