##uylar=[]
##for uy in range(10):
##    yangi_uy={
##        'yil':2010,
##        'deko':None,
##        'qavat':None,
##        'lokatsiya':'toshkent',
##        'hovli':None,
##        'narx':None,
##        }
##    
##    uylar.append(yangi_uy)
##    
##for uy in uylar[0:5]:
##    uy['deko']='evro',
##    uy['qavat']='2'
##    uy['narx']=100_000
##    uy['hovli']='yoq',
##    
##for uy in uylar[5:7]:
##    uy['hovli']='ha',
##    uy['deko']='oddiy',
##    uy['qavat']='1'
##    uy['narx']=110_000
##
##for uy in uylar[7:10]:
##    uy['hovli']='yoq',
##    uy['deko']='oddiy',
##    uy['qavat']='3'
##    uy['narx']=150_000
##    
##for uy in uylar[0:5]:
##    if uy['deko']=="evro":
##        uy['narx']=120_000
##    else:
##        uy['narx']=100_000
##
##print("Uylarimiz ro'yxati")
##for uy in uylar:
##    print(uy)
##shaxslar={
##    'elon_musk':'milliarder',
##    'hamdam_sobirov':"san'atkor",
##    'mrbeast':'youtuber',
##    'chris_Nolan':'rejissyor'
##    }
##print("Dunyodagi eng mashur insonlar")
##mashxur = [shaxslar]
##for key in mashxur:
##    print(f"Elon Mask {key['elon_musk']}, Hamdam Sobirov {key['hamdam_sobirov']}, MrBeast {key['mrbeast']}, \
##Christopher Nolan {key['chris_Nolan']}")
##dokon={'futbolka':100_000,
##       'shortik':95_000,
##       'kurtka':130_00,
##       'toppi':35_000,
##       }
##print("Kiyim-kechak do'konimiz mahsulotlari:")
##for kiyim in dokon.keys():
##    print(kiyim)
##

##savol="Istalgan son kiriting"
##savol+="(dasturni toxtatish un 'toxta' deb yozing):"
##qiymat=''
##while qiymat != 'toxta':
##    qiymat=input(savol)
##    if qiymat != 'toxta':
##        print(float(qiymat)**2)
##son=1
##while son>0:
##    son+=1
##    if son%2!=0:
##        continue
##    else:
##        print(son)

##kitoblar = []
##while True:
##    kitob = input("Yaxshi ko'rgan kitobingizni kiriting ('to'xta' deb yozsangiz, dasturni to'xtatadi): ")
##    if kitob.lower() == "to'xta":
##        break
##    else:
##        kitoblar.append(kitob)
##
##print("\nSiz kiritgan kitoblar:")
##for kitob in kitoblar:
##    print(kitob)

##son = 1
##while son>0: 
##    son += 1
##    if son%2!=0:
##        continue
##    else:
##        print(son)

##davlatlar=[]
##print("Biladigan davlatlaringizni nomlarini kiriting>")
##n=1 #narsa sanash uchun ozgaruvchi
##while True:
##    savol=f"{n}-Davlat nomini kiriting:"
##    davlat=input(savol)
##    davlatlar.append(davlat)
##    javob=input("Yana davlat qo'shasizmi? (ha/yoq)")
##    if javob=='ha':
##        n+=1
##        continue
##    else:
##        break
##
##print("Davlatlar ro'yxati:")
##for davlat in davlatlar:
##    print(davlat.title())

##print("Mashina va modellarini kiriting")
##mashinalar={}
##ishora=True
##while ishora:
##    mashina=input("Mashina nomini kiriting:")
##    model=input(f"{mashina.title()} ning modeli kiriting:")
##    mashinalar[mashina]=model #mashina kalit,model qiymat
##
##    javob=input("Yana mashina qo'shasizmi? (ha/yoq)")
##    if javob=="yoq":
##        ishora=False
##
##for mashina,model in mashinalar.items():
##    print(f"Siz kiritgan mashinalar ro'yxati:{mashina.title()} {model.title()} ")

#UV
#1-
##buyurtmalar=[]
##print("Buyurtmangizni kiriting.")
##n=1 
##while True:
##    ovqat=f"{n}-nima buyurtma qilasiz:"
##    buyurtma=input(ovqat)
##    buyurtmalar.append(buyurtma)
##    javob=input("Yana ovqat buyurtma qilasizmi? (ha/yo'q)")
##    if javob =='ha':
##        n+=1
##        continue
##    else:
##        break
##
##print("Buyurtmalaringiz ro'yxati:")
##for buyurtma in buyurtmalar:
##    print(buyurtma.title())

#2-
##print("Uzum Marketdagi bugungi mahsulotlar va narxlar ro'yxati:")
##items={}
##ishora=True
##while ishora:
##    item=input("Yangi mahsulot nomini kiriting:")
##    narx=input(f"{item.title()}ning narxini kiriting:")
##    items[item]=narx 
##
##    javob=input("Yana mahsulot qo'shasizmi? (ha/yoq)")
##    if javob=="yoq":
##        ishora=False
##
##for item,narx in items.items():
##    print(f"Siz kiritgan mahsulotlar ro'yxati:{item.title()}-{narx.title()}so'm. ")

#17-Dars
##talaba={"name":"Sherif",
##        "s_name":"Masharipov",
##        "yosh":"19",
##        "Iphone":False}
##talaba['married'] = True
##talaba["s_name"] = "Akbarov"
##talaba["yosh"] = 20
##talaba["Iphone"] = True
##del talaba["yosh"]
##print(talaba)

# fruits={"banan":10_000,
#        "mango":13_000}
# del fruits["banan"]
# for fruit,price in fruits.items():
#    print(f"Salom,do'konimizda {fruit} narxi {price} so'm")