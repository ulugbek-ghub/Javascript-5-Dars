#1)
import math
x = 8.38
# maxraj = 2 * math.tan(x + 2) - math.cos(x + 2)**x
# surat = 1 + math.cos(x + 2)**2
kasr1 = (math.sqrt(2 * math.tan(x + 2) - math.cos(x + 2)**x) / (1 + math.cos(x + 2)**2))
# kasr1 = math.sqrt(maxraj / surat)
kasr2 = math.sin(x**2) / (x **2 + 3)
misol = kasr1 + kasr2
print(misol)

#2)
# a = 0
# b = 1
# c = 5
# if a < b and b < c:
#     print("YESSS")
# else:
#     print("NOOO")

