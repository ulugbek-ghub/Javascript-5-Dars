# from uuid import uuid4
# class avto:
#     def __init__(self,make,model,rang,yil,narx,km=1000):
#         """Avto hususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narx = narx
#         self.__km = km
#         self.__id = uuid4()

#     def get_km(self):
#         return self.__km
#     def get_id(self):
#         return self.__id
    
#     def reduce_km(self, km):
#         """Moshinaning kmdan km olish"""
#         if km <= 0:
#             self.__km += km
#         else:
#             print("Moshinaning km qo'shib bolmaydi")

# class Kitob:
#     def __init__(self,nomi, muallif, yil, bet = 200):
#         """Avto hususiyatlari"""
#         self.nomi = nomi
#         self.muallif = muallif
#         self.yil = yil
#         self.__bet = bet

#     def get_bet(self):
#         return self.__bet
    
#     def add_bet(self, bet):
#         """Kitob betini o'zgartirish"""
#         if bet <= 0:
#             self.__bet += bet
#         elif bet >= 0:
#             self.__bet += bet
#         else:
#             print("Kitob betini qo'shib bo'lmaydi")

#Uyga vazifa
# class Shaxs:
#     """Shaxslar haqida ma'lumot"""
#     def __init__(self,ism,familiya,passport,tyil, kurs = 1):
#         self.ism = ism
#         self.familiya = familiya
#         self.passport = passport
#         self.tyil = tyil

#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
#         return info
        
#     def get_age(self,yil):
#         """Shaxsning yoshini qaytaruvchi metod"""
#         return yil - self.tyil

# class Talaba(Shaxs): ## bu shaxs CLASS super class deb ataladi, Talaba voris class deb ataladi
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,passport,tyil,idraqam):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.__kurs = kurs

#     def get_kurs(self):
#         return self.__kurs

#     def change_kurs(self, kurs):
#         """Talaba kursini ozgartirish"""
#         if kurs <= 0:
#             self.__kurs += kurs
#         elif kurs >= 0:
#             self.__kurs += kurs
#         else:
#             print("Kursni o'zgartirib bolmaydi")

#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
#         return info