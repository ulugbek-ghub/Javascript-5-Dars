##import math
##def kv_teng(a,b,c):
##    D = b**2 - 4*a*c
##    if D < 0:
##        return "Ildiz mavjud emas"
##    t1 = (-b + math.sqrt(D))/(2*a)
##    t2 = (-b - math.sqrt(D))/(2*a)
##
##    ildizlar = set()
##
##    for x in (t1,t2):
##        if x >= 0:
##            ildizlar.add(math.sqrt(x))
##            ildizlar.add(-math.sqrt(x))
##    if ildizlar:
##        return f"Ildizlar: {sorted(ildizlar)}"
##    else:
##        return "Ildizlar yoq"


# def qoshuvchirial(son):
#     qoshuvchi = 1
#     for i in range(1,son+1):
#         qoshuvchi *=i
#     return qoshuvchi

# import math
# print(math.lcm(12, 15))


##def qoshuvchi(n):
##    for i in range()


# def faktorial(son):
#     qoshuvchi = 0
#     for i in range(1,son+1):
#         qoshuvchi +=i
#     return qoshuvchi


# listt = [3,4,6,9,12,-2]
# listt.sort()
# print(listt[1])



def orta(a,b):
    return f"Orta arifmetik: {round((a+b)/2)}"
print(orta(3,5))
