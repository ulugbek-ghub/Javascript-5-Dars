# file.rstrip() - bu faylning oxiridagi bo'sh joylarni olib tashlaydi
# file.replace('\n', '') - bu faylning ichidagi Enter larni olib tashlaydi

##with open("Sonlar.txt") as file:
##    sonlar = file.read()
##print(sonlar)

##sonlar = sonlar.rstrip()
##sonlar = sonlar.replace("\n", "")
##sonlar = float(sonlar)
##print(sonlar)

filename = "mashinalar/cars.txt"
##with open(filename) as file:
##    for line in file:
##        print(line)

with open(filename) as file:
    cars = file.readlines()
print(cars)

cars = [car.rstrip() for car in cars]
print(cars)
