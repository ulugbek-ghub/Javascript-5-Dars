import math
#1)
surat = (math.sqrt(4 - 1) + math.sqrt(4 + 2) + math.log10(math.sqrt(1.28 * pow(4, 2) + 2)))
maxraj = (math.sqrt(4 + 2) + math.sqrt(4 + 24) + pow(4, 5))
x = surat / maxraj
print(x)

#2)
print(max(3.96, 3.58, 2.83), min(3.96, 3.58, 2.83))

#3)
print(max(0 + -4 + -1, 0, -4, -1), min((0 + -4) / 2, 0, -4, -1) ** 2)

#4)
x = ((math.sqrt(16) / pow(125,1/3) + math.log10(1000) - 3 * math.pi)  /  ( (pow(16,1/4) / pow(243,1/5)) + abs(-2) )) * pow(3,2)
print(x)

#5)
x = ((math.sqrt(pow(2,1/4)) + math.log2(32) + math.sqrt(25) / pow(8,1/3) - math.log10(100)) / (abs(-3) + 2 * math.pi)) * pow(1000,1/3)
print(x)
