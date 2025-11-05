class AVTO:
    """Avto klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avto hususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx

    # def __str__(self):
    #     """Avto haqida ma'lumot"""
    #     return f"{self.rang} {self.make} {self.model}, {self.yil} - yil, Narxi: {self.narx} $"

## Repr yaxshiroq
    # def __repr__(self):
    #     """Avto haqida ma'lumot"""
    #     return f"{self.rang} {self.make} {self.model}, {self.yil} - yil, Narxi: {self.narx} $"

# self > y, avto1 > avto2
    # def __lt__(self, y):
##        return self.model < y.model
##    def __le__(self, y):
##        return self.narx <= y.narx
##    def __gt__(self, y):
##        return self.narx > y.narx
##    def __ge__(self, y):
##        return self.narx >= y.narx
##    def __eq__(self, y):
##        return self.narx == y.narx
##    def __ne__(self, y):
##        return self.narx != y.narx

#avto1 = AVTO("GM", "Malibu", "Qora", 2023, 40000)
#avto2 = AVTO("GM", "Cobalt", "Oq", 2025, 15000)

class Talaba: ## bu shaxs CLASS super class deb ataladi, Talaba voris class deb ataladi
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.idraqam = idraqam

    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    def __lt__(self, y):
        return self.tyil < y.tyil
    def __gt__(self, y):
        return self.tyil > y.tyil
    def __eq__(self, y):    
        return self.tyil == y.tyil
    def __ne__(self, y):
        return self.tyil != y.tyil
    def __le__(self, y):
        return self.tyil <= y.tyil
    def __ge__(self, y):
        return self.tyil >= y.tyil
talaba1 = Talaba("Alijon", "Valiyev", "AA1234567", 2000, 123456)
talaba2 = Talaba("Valijon", "Olimov", "AA7654321", 1995, 654321)
