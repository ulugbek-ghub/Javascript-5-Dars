# x,y,z, = 0.43, 1.11, 0.75

# def uzgartir(a,b,c,d):
#     if a<=b<=c<=d:
#         katta =  max(a,b,c,d)
#         return katta, katta, katta, katta
#     else:
#         kichik = min(a,b,c,d)
#         return kichik,kichik,kichik,kichik

# def sonlar(a,b,c):
    
# def sonlar(a,b):
#     if a <= b:
#         a = 0
#         return a,b
#     else:
#         return a,b 



#Kiruvchi ma’lumotlar: -13.07 6.16
#Chiquvchi ma’lumotlar: -12.57 6.66
#1)
def sonlar(x,y):
    if x < 0 and y < 0:
        x = abs(x)
        y = abs(y)
        return x,y
    elif x < 0 or y < 0:
        x += 0.5
        y += 0.5
        return x,y
    else:
        return x,y

#2)
# def uchburchak(x,y,z):
#     if x+y>z and x+z>y and y+z>x:
#         return "YES"
#     else:
#         return "NO"

