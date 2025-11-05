# isinstance - tegishlimi?

class AVTO:
    """Avto klassi"""
    def __init__(self,make,model,rang,yil,narx):
        """Avto hususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
    def __repr__(self):
       return f"Avto: {self.make} {self.model} {self.rang} mashina"

class AVTOSALON:
    """AvtoSalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        """Avto haqida ma'lumot"""
        return f"{self.name} avtolari"

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, qiymat):
        self.avtolar[index] = qiymat

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, AVTO):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting")



salzon1 = AVTOSALON("GM")    

avto1 = AVTO("GM", "Malibu", "Qora", 2023, 40000)
avto2 = AVTO("GM", "Cobalt", "Oq", 2025, 15000)

salon1.add_avto(avto1, avto2)
