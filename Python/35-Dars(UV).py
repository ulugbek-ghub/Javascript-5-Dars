class TALABA:
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,bosqich):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.idraqam = idraqam
        self.bosqich = bosqich



    def __repr__(self):
        return f"{self.ism} {self.familiya}"

## Yil solishtirish
    # def __lt__(self, y):
    #     return self.tyil < y.tyil
    # def __gt__(self, y):
    #     return self.tyil > y.tyil
    # def __eq__(self, y):    
    #     return self.tyil == y.tyil
    # def __ne__(self, y):
    #     return self.tyil != y.tyil
    # def __le__(self, y):
    #     return self.tyil <= y.tyil
    # def __ge__(self, y):
    #     return self.tyil >= y.tyil
## Bosqich solishtirish
    def __lt__(self, y):
        return self.bosqich < y.bosqich
    def __gt__(self, y):
        return self.bosqich > y.bosqich
    def __eq__(self, y):
        return self.bosqich == y.bosqich
    def __ne__(self, y):
        return self.bosqich != y.bosqich
    def __le__(self, y):
        return self.bosqich <= y.bosqich
    def __ge__(self, y):
        return self.bosqich >= y.bosqich


talaba1 = TALABA("Alijon", "Valiyev", "AA1234567", 2000, 123456, 4)
talaba2 = TALABA("Valijon", "Olimov", "AA7654321", 1995, 654321, 3)

class KITOB:
    def __init__(self, nomi, bet, summa):
        self.nomi = nomi
        self.bet = bet
        self.summa = summa

##  summa solishtirish
    def __lt__(self, y):
        return self.summa < y.summa
    def __gt__(self, y):
        return self.summa > y.summa
    def __eq__(self, y):
        return self.summa == y.summa
    def __ne__(self, y):
        return self.summa != y.summa
    def __le__(self, y):
        return self.summa <= y.summa
    def __ge__(self, y):
        return self.summa >= y.summa

##  bet solishtirish
    def __lt__(self, y):
        return self.bet < y.bet
    

kitob1 = KITOB("Shum Bola", 300, 100000)
kitob2 = KITOB("Ufq 1-kitob", 350, 90000)