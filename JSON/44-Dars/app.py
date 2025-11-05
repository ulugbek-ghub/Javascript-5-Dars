# filename = 'text.txt'
# with open(filename) as file_object:
#     text = f.read()

# filename = 'data.txt'
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechrasiz,{filename} fayli topilmadi.Boshqa fayl kiriting")

# n = input("Yoshingizni kiriting: ")
# try:
#     n= int(n)
#     x= 2025 - n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 dan ayirib bo'lmaydi")
# else:
#     print(f"Tu'gilgan yilingiz: {x}-yil!")

# import json

# car1 = {
#     'model': 'Cobalt',
# }

# car1_json = json.dumps(car1,indent=4)
# with open('car1.json', 'w') as f:
#     json.dump(car1, f)



                                                    
# files = ['car1.json', 'car2.json', 'car3.json']
# for file in files:
#     try:
#         with open(file) as f:
#             car = json.load(f)
#     except FileNotFoundError:
#         pass
#     else:
#         print(car1['model'])

# var.isdigit() - bu funksiya faqat raqamlarni qabul qiladi

while True:
    yosh = input("Yoshingizni kiriting: ")
    if yosh.isdigit():
        yosh = int(yosh)
        break
    else:
        yosh = round(float(yosh))
        break
print(f"Siz {2025-yosh} yilda tug'ilgansiz")