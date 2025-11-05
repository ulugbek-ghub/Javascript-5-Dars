# son=int(input("2025-yildagi son kiriting:"))
# if son % 7 == 1:
#     print(f"2025-yilda {son}-kun-Dushanba kuni.")
# elif son % 7 == 2:
#     print(f"2025-yilda {son}-kun-Seshanba kuni.")
# elif son % 7 == 3:
#     print(f"2025-yilda {son}-kun-Chorshanba kuni.")
# elif son % 7 == 4:
#     print(f"2025-yilda {son}-kun-Payshanba kuni.")
# elif son % 7 == 5:
#     print(f"2025-yilda {son}-kun-Juma kuni.")
# elif son % 7 == 6:
#     print(f"2025-yilda {son}-kun-Shanba kuni.")
# elif son % 7 == 7:
#     print(f"2025-yilda {son}-kun-Yakshanba kuni.")
# else:
#     print("Bu kun mavjud emas")

son = int(input("2025-yildagi son kiriting: "))
if son % 7 == 1:
    print(f"2025-yilda {son}-kun-Dushanba kuni.")
elif son % 7 == 2:
    print(f"2025-yilda {son}-kun-Seshanba kuni.")
elif son % 7 == 3:
    print(f"2025-yilda {son}-kun-Chorshanba kuni.")
elif son % 7 == 4:
    print(f"2025-yilda {son}-kun-Payshanba kuni.")
elif son % 7 == 5:
    print(f"2025-yilda {son}-kun-Juma kuni.")
elif son % 7 == 6:
    print(f"2025-yilda {son}-kun-Shanba kuni.")
elif son % 7 == 0:  # Replace 7 with 0
    print(f"2025-yilda {son}-kun-Yakshanba kuni.")
else:
    print("Bu kun mavjud emas")