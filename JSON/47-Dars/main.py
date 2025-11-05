# import datetime 

# hozir = datetime.datetime.now()
# print(hozir)

# print(hozir.date())

# print(hozir.time())

# print(hozir.hour)

# print(hozir.minute)

# print(hozir.second)

# import datetime as dt

# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# vaqthozir = hozir.time()
# print(f"Hozir soat {vaqthozir}")

# bugun = dt.date.today()
# aksiya_vaqti = dt.date(2025,4,1)
# farq = aksiya_vaqti_bugun
# print(f"Aksiya tugashiga {farq.days} kun qoldi")

# hozir = dt.datetime.now()
# futbol = dt.datetime(2025,3,3,23,45,00)
# farq = futbol-hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {sekundlar} sekund qoldi")
# print(f"Futbol boshlanishiga {minutlar} minut qoldi")
# print(f"Futbol boshlanishiga {soatlar} soat qoldi")

#1)

# import datetime

# hozir = datetime.datetime.now()
# ramazon = datetime.datetime(2025,3,31,23,59,59)
# farq = ramazon-hozir
# print(f"Ramazon tugashiga {farq.days} kun qoldi")


#2)

# import datetime
# bugun = datetime.date.today()
# hafta = datetime.timedelta(days=14)
# print(bugun)
# for i in range(10):
#     bugun += hafta
#     print(bugun)