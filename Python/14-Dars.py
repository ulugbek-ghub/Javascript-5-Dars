#dokon={
#    "olma":12000,
#    "anor":15000,
#    "banan":14000,
#    "mango":20000
#}
#for k,q in dokon.items():
#    print(f"Korzinkaga xush kelibsiz,meva qismimizda yangi narxlar,\
#yangi mahsulotlar!")
#    print(f"Do'konimizda {k.title()} {q} so'm")

dokon={'futbolka':100_000,
       'shortik':95_000,
       'kurtka':130_00,
       'toppi':35_000,
       }
print("Kiyim-kechak do'konimiz mahsulotlari:")
for kiyim in dokon.keys():
    print(kiyim)

print("Mening bozorlik ro'yxatim:")
bozorlik=['futbolka','shortik','krossovka']
for kiyim in dokon:
    if kiyim in bozorlik:
        print(f"{kiyim.title()} {dokon[kiyim]} so'm")
for buyum in bozorlik:
    if buyum not in dokon:
        print(f"Do'koningizga {buyum} dan keltirib qo'ying!")