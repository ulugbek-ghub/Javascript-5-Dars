#mevalar={"olma":10000,"uzum":13000,"anor":15000}
#print(f"olma narxi {mevalar['olma']} som turadi")
#print(f"uzum narxi {mevalar['uzum']} som turadi")
#print(f"anor narxi {mevalar['anor']} som turadi")

#talaba_0={'ism':"Rejafboy Masharipov"}
#talaba_0['ism']='rejji chish'
#print(talaba_0)
#telefonlar={
#    'ali':'iphone 16',
#    'vali':'mi90 pro',

#mevalar={"anor":15000,"uzum":13000,"olma":10000,'tarvuz':2000,'qovun':1700}
#del mevalar['anor']
#mevalar['tarvuz']=1500

#mevalar['sabzi']=3000

#print(mevalar)

#UYGA VAZIFA---------------------------------------
#ota={"otam":Otabek Safarboyev,
#     "yoshi":45,
#     "tug'ilgan yili":1979,
#     'manzili':urganch tumani,
#     }
#print("Otamning ismi {ota[otam]},yoshi{ota[yoshi]}da,{ota[tug'ilgan yili]}-yili,{ota[manzili]} da tavallud topgan!")  

#sev_taom={
#    'Akam': 'Osh',
#    'Opom': 'Somsa',
#    'Buvim': 'Shorva'
#    }
#print(f"Buvimning sevimli taomi {sev_taom['Buvim']}")

soz={
     "toyota":"Supra",
     "hissan":"R34",
     "honda":"NSX",
     "mazda":"RX7",
     "bmw":"M4",}
cars=input("Mashina nomini kiriting")
moshina = soz.get(cars)
if soz==None:
    print("Bu mashina bilmayman,borib Googledan so'ra")
else:
    print(f"Siz so'ragan mashina {moshina}")
