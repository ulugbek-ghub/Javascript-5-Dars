
# #2)
# filename = "get_info.txt"

# ism = input("Ismingizni kiriting: ")
# fam = input("Familiyangizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")

# with open(filename, 'a') as file:
#     file.write(f"Sizning ismingz: {ism} \n")
#     file.write(f"Sizning familyangiz {fam} \n")
#     file.write(f"Sizning yoshingiz: {yosh} \n")

with open('pi_million_digits.txt') as file:
    pi = float(file.read())
print(round(pi,3))
