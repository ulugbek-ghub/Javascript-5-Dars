# class Car:
#     def __init__(self, rusum, rangi, korobka):
#         self.rusum = rusum
#         self.rangi = rangi
#         self.korobka = korobka
#         self.yil = 2020

#     def car_info(self):
#         return f"Mashina rusumi {self.rusum}, rangi {self.rangi}, ishlab chiqarilgan yili {self.yil}-yil va korobka turi {self.korobka}"

#     def set_yil(self, yil):
#         self.yil = yil

# car1 = Car("Nexia", "Oq", "avto")
# car2 = Car("Malibu", "Qora", "mexanika")

# # car1.set_yil(2015)
# print(car1.car_info())




# class dost:
#     def __init__(self, ism, fam, yosh, harakter):
#        self.ism = ism
#        self.fam = fam
#        self.yosh = yosh
#        self.harakter = harakter
#        self.sev_oyin = "Fifa Mobile"
   
#     def tanishtir_dost(self):
#        return f"Salom, mening do'stimning ismi {self.ism}, familiyasi {self.fam},{self.yosh} yoshda, harakteri {self.harakter}, sevimli o'yini {self.sev_oyin}."

#     def set_sev_oyin(self, sev_oyin):
#         self.sev_oyin = sev_oyin

# dost1 = dost("Og'abek", "Bahodirov", 17 , "chill")
# dost1.set_sev_oyin("GTA Vice City")
# dost2 = dost("Ali", "Valiyev", 18, "qiziq")
# dost2.set_sev_oyin("PUBG")
# print(dost1.tanishtir_dost())
# print(dost2.tanishtir_dost())

#1)
# class kitobs:
#     def __init__(self, nomi, muallif, nashr_yili):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yili = nashr_yili
#         self.sahifa_son = 200
#         self.narx = 15000
#     def kitob_info(self):
#         return f"Kitob nomi: {self.nomi}, muallifi: {self.muallif}, nashr yili: {self.nashr_yili}, sahifa soni: {self.sahifa_son}, narxi: {self.narx}"
#     def set_narx(self, narx, sahifa_son):
#         self.narx = narx
#         self.sahifa_son = sahifa_son
#         
# kitob1 = kitobs("Dyuna", "Frank Herbert", 1965)
# kitob1.set_narx(20000)
# kitob2 = kitobs("Shum bola", "G'ofur G'ulom", 1990)
# kitob2.set_sahifa_son(250)
# print(kitob1.kitob_info())
# print(kitob2.kitob_info())

#2) 
# class telefon:
#     def __init__(self, firma, firma, rangi, narx):
#         self.firma = firma
#         self.firma = firma
#         self.rangi = rangi
#         self.narx = 300
#         self.olcham: 6.1
#         self.processor = 12
#     def tel_info(self):
#         return f"Telefon: {self.firma}, firma: {self.firma}, rangi: {self.rangi}, narxi: {self.narx}, olchami: {self.olcham}, processor: {self.processor}"
#     def set_olcham(self, olcham):
#         self.olcham = olcham
#     def set_processor(self, processor):
#         self.processor = processor

# tel1 = telefon("Samsung", "Galaxy S25", "Qora", 800)
# tel1.set_olcham(6.8)
# tel1.set_processor(16)
# tel2 = telefon("Iphone", "16 Pro max", "Oq", 1200)
# tel2.set_olcham(6.5)
# tel2.set_processor(12)
# print(tel1.tel_info())
# print(tel2.tel_info())

#3)
# class komp:
#     def __init__(self, plata, firma, narx):
#         self.firma = firma
#         self.plata = plata
#         self.narx = narx
#         self.hdd = "2GB"
#         self.processor = "Intel Core i5"
#     def komp_info(self):
#         return f"Komputer: {self.firma}, firma: {self.firma}, processor: {self.processor}, hdd: {self.hdd}, narxi: {self.narx}"    
#     def set_narx(self, processor):
#         self.processor = processor
#     def set_hdd(self, hdd):
#         self.hdd = hdd
# komp1 = komp("Acer", "Aspire 7", 800)
# komp2 = komp("ROG", "Zephyrus G14", 1400)
# komp1.set_narx("Intel Core i7")
# komp1.set_hdd("8GB")
# komp2.set_narx("Intel Core i9")
# komp2.set_hdd("16GB")
# print(komp1.komp_info())
# print(komp2.komp_info())