# son1 = input("1-sonni kiriting: ")
# son2 = input("2-sonni kiriting: ")
# if son1 == son2:
#     print("Sonlar teng")
# elif son1 > son2:
#     print(f"{son1} > {son2} dan katta")
# else:
#     print(f"{son2} > {son1} dan katta")

# kitoblar = []
# kitob = input(f"Kitob kiriting: ")
# while True:
#     if kitob != "stop":
#         kitoblar.append(kitob)
#         kitob = input(f"Kitob kiriting: ")
#     else:
#         print(kitoblar)
#         break

# def shaxs():
#     """Shaxs haqida malumot"""
#     ism = input("Ismingizni kiriting: ")
#     yosh = int(input("Yoshingizni kiriting: "))
#     print(f"Ismingiz - {ism} va {2025 - yosh} yilda tug'ilgansiz")

# def son_kopaytir():
#     """Sonni kvadrati va kubi"""
#     son = int(input("Sonni kiriting: "))
#     print(f"Kvadrati: {pow(son,2)}, kubi: {pow(son,3)}")
# son_kopaytir()

import math
a = 20
b = 5
misol = abs(-4) + (pow(25 * (math.sqrt(a+b)),1/3)) / (abs(-a) + math.log2(8))
print(misol)