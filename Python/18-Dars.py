son=int(input("Har qanday son kiriting va shu sonni kvadrati va kubini chiqarib beraman:"))
def son_kvad_kub(son):
    """Sonni kvadrati va kubini chiqaradigan funksiya"""
    print(f"{son} ning kvadrati:{son ** 2} ga, kubi esa: {son ** 3} ga teng")
son_kvad_kub(son)

# def son_kopaytir(son):
#     """Sonni 2,4,5,7,9 ga kopaytiradigan funksiya"""
#     print(f"{son} 2 ga bo'linsa {son / 2} boladi,"
# f"{son} 4 ga bo'linsa {son / 4} boladi,")

#UYGA VAZIFA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 1)
# ism=input("Ismingizni kiriting> ")
# yosh=int(input("Yoshingizni kiriting> "))
# def ism_yosh(ism,yosh):
#     """Ism va yosh kiritib tugilgan yilni chiqarib baradigan funksiya"""
#     print(f"Salom {ism.title()},sen {2024-yosh}-yilda tug'ilgansan!")
# ism_yosh(ism,yosh)

# 2)
# def kvadrat_kub(son):
#     """Sonni kvadrati bilan kubini chiqaradigan funksiya"""
#     print(f"{son} ning kvadrati {son ** 2} ga, kubi {son ** 3} ga teng")
# kvadrat_kub(712)

# 3)
# def son_juft_toq(son):
#     """Sonni juft yoki toqligini topadigan funksiya"""
#     if son % 2 == 0:
#             print(f"{son} soni juft")
#     else:
#             print(f"{son} soni toq")
# son_juft_toq(9)

# 4)Xato chiqib duribdi:(
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# def katta_kichik():
#     """Sonnlar bir biridan katta yoki kichiklikini aniqlaydigan funksiya:)"""
#     if son1 > son2:
#         print(f"{son1} {son2} dan katta")
#     elif son2 > son1:
#         print(f"{son2} {son1} dan katta")
#     else:
#         print(f"Sonlar bir biriga teng:{son1}={son2}")
# katta_kichik()