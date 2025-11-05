# Value error - xatosi kopincha biror qiymatni notogri turda yoki kutilmagan formatda
# berishdan kelb chiqadi

# try - harakat
# except - aks holda (lekin)

# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2025-yosh}-yilda tug'ilgansiz")
# print("Dastur tugadi")

# yil = input("Tug'ilgan yilingizni kiriting: ")
# try:
#     yil = int(yil)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2025-yil} yoshdasiz!")
# print("Dastur tugadi!")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# try:
#     print(cars[9])
# except IndexError:
#     print(f"Ro'yxatda {len(cars)} ta mashina bor xolos")

# user = {
#     'username': 'farrux',
#     'status': 'admin',
#     'phone': '998977777777'
#     }

# key = 'tel'
# print(f"Foydalanuvchi: {user[key]}")



#1) KeyError
cobalt = {
    'model': 'cobalt',
    'rang': 'qora',
    'yil': 2018,
    'narh': 12000
}

key = 'narh'
try:
    print(f"Mashina {cobalt[key]} dollar")
except KeyError:
    print("Bunday kalit mavjud emas")
print('')

#2) ValueError
# yil = input("Tug'ilgan yilingizni kiriting: ")
# try:
#     yil = int(yil)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2025-yil} yoshdasiz!")
# print("Dastur tugadi!")

#3) IndexError
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# try:
#     print(cars[9])
# except IndexError:
#     print(f"Ro'yxatda {len(cars)} ta mashina bor xolos")

#4) ZeroDivisionError
# son = input("Son kiriting: ")
# try:
#     son = int(son)
#     print(son/0)
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas")
# print("Dastur tugadi")