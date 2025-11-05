class Talaba:
   def __init__(self, ism, familiya, tyil):
       self.ism = ism
       self.familiya = familiya
       self.tyil = tyil
   def tanishtir(self):
       print(f"Ismim {self.ism}, familiyam {self.familiya}, Yoshim{2025 - self.tyil}da")

Talaba1 = Talaba("Asad", "Komilov", 2009)


# class avto_info:
#     def __init__(self, rusm, korobka, chyil, rang):
#         self.rusm = rusm
#         self.korobka = korobka
#         self.chyil = chyil
#         self.rang = rang

#     def toliq_info(self):
#         print(f"Bu mashina {self.chyil}-da ishlab chiqarilgan,rusmi {self.rusm},{self.korobka} korobkasi bor va rangi {self.rang}.")
# avto1 = avto_info("Cobalt", "avto", 2020, "oq")
# print(avto1.toliq_info())

#UV
#1)
# class user:
#     def __init__(self, u_name, email, p_word):
#         self.u_name = u_name
#         self.email = email
#         self.p_word = p_word

#     def user_info(self):
#         print(f"Salom, {self.u_name}. Sizning pochtangiz:{self.email} va parolingiz:{self.p_word}.")

# user1 = user("milliycoder", "hasanvaliyev827@gmail.com", "hasan827") #user1.user_info()