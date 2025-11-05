# svetafor = 'qizil'
# match svetafor:
#     case 'qizil':
#         print('Turing')
#     case 'sariq':
#         print('Tayyorlaning')
#     case 'yashil':
#         print('Yurish')
#     case _:
#         print('Xato rang')

# hafta = 4
# def hafta_kun(son):
#     match son:
#         case 1 | 8 | 9:
#             print('Dushanba')
#         case 2:
#             print('Seshanba')
#         case 3:
#             print('Chorshanba')
#         case 4:
#             print('Payshanba')
#         case 5:
#             print('Juma')
#         case 6:
#             print('Shanba')
#         case 7:
#             print('Yakshanba')


# oylar = 'Mart'
# match oylar:
#     case 'Dekabr' | 'Yanvar' | 'Fevral':
#         print('Hozir Qish fasli')
#     case 'Mart' | 'Aprel' | 'May':
#         print('Hozir Bahor fasli')
#     case 'Iyun' | 'Iyul' | 'Avgust':
#         print('Hozir Yoz fasli')
#     case 'Sentabr' | 'Oktabr' | 'Noyabr':
#         print('Hozir Kuz fasli')


##def baho(ball):
##    match ball:
##        case 5:
##            print('Juda yaxshi')
##        case 4:
##            print('Yaxshi')
##        case 3:
##            print('Qoniqarli')
##        case 2:
##            print('Qoniqarsiz')
##        case 1:
##            print('Maktabdan get uka!')
##        case _:
##            print("Baho olasanmi o'zi?")



# def sonlar(son):
#     match son % 2:
#         case 0:
#             print('Juft son')
#         case 1:
#             print('Toq son')


# def calc(a,b,amal):
#     match amal:
#         case '+':
#             return a + b
#         case '-':
#             return a - b
#         case '*':
#             return a * b
#         case '/':
#             return a / b if b != 0 else "0 ga bo'linmaydi"
#         case _:
#             return "Xato amal"
# a = round(float(input('a = ')))
# b = round(float(input('b = ')))

# amal = input('Amalni kiriting: ')
# print(calc(a,b,amal))


def tala_ball(ball):
    match ball:
        case _ if 90 <= baho < 100:
            print("A'lo")
        case _ if 90 <= baho < 75:
            print("Yaxshi")
        case _ if 75 <= baho < 60:
            print("Qoniqarli")
        case _ if 60 <= baho < 40:
            print("Qoniqarsiz")
        case _:
            print('Juda past baho')
