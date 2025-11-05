# *Args parametrlarda ishlariladi 
#o'zgarmas royxatga (tuple)
# def summa (*sonlar):
#     """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print((summa))

#Agar funksiya bir nechta argument qabul qilsa, *args argument doim oxirida boladi

# def summa(x,y,*Z):
#     """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
#     return x+y+sum(Z)
# print(summa(2,4,32723482648234897494823))

# **kwargs-keyword arguments (kalit so'zli argumentlar)

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi malumotlarni lugat korinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1=avto_info("GM",'malibu',rang='qora', yil=2018,narx=35000)
# avto2=avto_info("Kia","K5",rang='oq', yil=2020,narx=45000)

# print(avto1)
# print(avto2)


#UV:
#1)
def summa(*son):
    """Kiritilgan sonlar yigindisini hisoblaydigan funksiya"""
    return sum(son)
sonlar=[]
print('')
print("Sonlarni birma-bir kiriting (tugatish uchun 'stop' deb yozing):")

while True:
    son = input(f"Keyingi sonni kiriting: ")
    if son.lower() == 'stop':
        break
    try:
        sonlar.append(int(son))
    except ValueError:
        print("Iltimos, faqat son kiriting yoki 'stop' deb yozib tugating.")
natija = summa()
print(f"Kiritilgan sonlar yig'indisi: {natija}")

#3)
def talaba_info(ism, fam, tug_yil, tug_joy, jinsi=''):
    """Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumot = {
        'ism': ism,
        'fam': fam,
        'tug_yil': tug_yil,
        'tug_joy': tug_joy,
        'jinsi': jinsi
    }
    return malumot

talaba1 = talaba_info('Husan', 'Sharipov', '2001', 'Buxoro', 'erkak')

print(talaba1)

#4)
def dost(ism,fam,yil,**malumotlar):
    """Do'stingiz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism'] = ism
    malumotlar['fam'] = fam
    malumotlar['yil'] = yil
    return malumotlar

dost1 = dost("Musobek", "To'liyev", 2010, boy=1.64, tug_joy="Urgench")
print(dost1)

