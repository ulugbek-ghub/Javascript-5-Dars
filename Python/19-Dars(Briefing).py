# usd=int(input("Dollarda pul kiriting: "))
# def usd_usz():
#     """USD ni somga aylanitiradigan funksiya"""
#     print(f"{usd} dollar + 2.000.000 so'm = {usd * 13_000 + 2_000_000} so'm")
# usd_usz()

# def son_kvad(son):
#     """sonni 3-darajasi bilan 7-darajasini topib beradi"""
#     print(f"{son ** 3} {son ** 7}")

#3)
# print("Bugungi yangi kelgan mahsulotlar va narxlar ro'yxati:")
# items={
#     "futbolka":100_000,
#     "noski":10_000
# }
# ishora=True
# while ishora:
#    item=input("Yangi mahsulot nomini kiriting:")
#    narx=input(f"{item.title()}ning narxini kiriting:")
#    items[item]=narx
# if item in items:
#     print("Bu mahsulot allaqachon do'konga olib kelingan")
# else:
#     javob=input("Yana mahsulot qo'shasizmi? (ha/yoq)")
#     if javob=="yoq":
#        ishora=False
#     else:
#         print("Bu mahsulot allaqachon do'konga olib kelingan")

# for item,narx in items.items():
#    print(f"Siz kiritgan yangi mahsulotlar ro'yxati:{item.title()}-{narx.title()}so'm. ")