# class Sinf:
#     def __init__(self, sinf_nomi, etaj, student_soni):
#         self.sinf_nomi = sinf_nomi
#         self.etaj = etaj
#         self.student_soni = student_soni

# ##def __repr__(self):
# ##    return f"Bizning sinf:{self.sinf_nomi},{self.etaj}-etajda joylashgan va {self.student_soni} ta o'quvchi bor"
#     def __gt__(self, y):
#         return self.student_soni > y.student_soni
    
# sinf1 = Sinf("8D", 2, 29)
# sinf2 = Sinf("8A", 1, 33)


# from uuid import uuid4
# class MAKTAB:
#     '''Maktab klassi'''
#     def __init__(self, nomi, manzil, raqam, sinf):
#         '''Maktab xususiyatlari'''
#         self.nomi = nomi
#         self.__manzil = manzil
#         self.__raqam = raqam
#         self.__id = uuid4()
#         self.sinf = sinf
#     def get_manzil(self):
#         return self.__manzil
#     def get_raqam(self):
#         return self.__raqam
#     def get_id(self):
#         return self.__id

#     def set_raqam(self, raqam):
#         '''Maktab raqamini o'zgartirish'''
#         if raqam <= 0:
#             self.__raqam += raqam
#         elif raqam >= 0:
#             self.__raqam += raqam
#         else:
#             print("Maktab raqamni o'zgartirib bolmaydi")
        
# mk1 = MAKTAB("Nizomiy", "Urganch tumani", 1, "8D")
# mk2 = MAKTAB("Nizomiy", "Urganch tumani", 2, "8A")