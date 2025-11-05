class Car:
    def __init__(self, rusum, rangi, korobka):
        self.rusum = rusum
        self.rangi = rangi
        self.korobka = korobka
        self.yil = 2020

    def car_info(self):
        return f"Mashina rusumi {self.rusum}, rangi {self.rangi}, ishlab chiqarilgan yili {self.yil}-yil va korobka turi {self.korobka}"

    def set_yil(self, yil):
        self.yil = yil

car1 = Car("Nexia", "Oq", "avto")
car2 = Car("Malibu", "Qora", "mexanika")


class car_royxat():
    def __init__(self, rusum):
        self.rusum = rusum
        self.car_soni = car_soni
        self.car = []

    def add_car(self, car):
        """Mashinalarni ro'yxatga qo'shish"""
        self.car.append(car)
        self.car_soni += 1
