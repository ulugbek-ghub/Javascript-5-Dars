# class Kitob:
#     """Kitob haqida malumot"""
#     def __init__(self, nomi, muallif, nashr_yil):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yil = nashr_yil
    
#     def get_yil(self):
#         return f"{self.nomi} {self.nashr_yil}-yilda chiqqan"
#     def get_muallif(self):
#         return f"{self.nomi} {self.muallif} tomonidan yozilgan"
#     def nashr_yil(self):
#         return f"{self.nomi} {self.nashr_yil}-yilda nashr qilingan"
#     def get_info(self):
#         """Shaxs haqida ma'lumot"""
#         info = f"{self.nomi} {self.muallif}."
#         info += f"{self.nomi}:{self.muallif}, {self.nashr_yil}-yilda nashr qilingan"
#         return info


# class Kitob_Super(Kitob):
#     """Kitob super klassi"""
#     def __init__(self, nomi, muallif, nashr_yil, narxi):
#         super().__init__(nomi, muallif, nashr_yil,)
#         self.narxi = 30

#     def set_narxi(self):
#         self.narxi = narxi
#     def get_narxi(self):
#         return f"{self.nomi} {self.narxi} dollar turadi. "
#     def get_info(self):
#         info = f" {self.nomi}:{self.muallif},narxi:${self.narxi}, {self.nashr_yil}-yilda nashr qilingan"
#         return info

# kitob1 = Kitob_Super("Dunyoning ishlari", "O'tkir Hoshimov", 2004, 30)
# print(kitob1.get_info())


class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs): ## bu shaxs CLASS super class deb ataladi, Talaba voris class deb ataladi
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar = []

    def fanga_yozil(self,fan):
        """Talabani fanga yozish"""
        self.fanlar.append(fan)

    def get_fanlar(self):
        """Talaba o'qiydigan fanlari"""
        return self.fanlar    

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}. O'qiydigan fani: {self.fanlar}"
        return info
