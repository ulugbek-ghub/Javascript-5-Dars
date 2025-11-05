narx = 0

tovuq_shorva=15000
choy=4000
non=3000
salat=5000
coca_cola=5000

tovuq_shorva = input("Tovuq sho'rva olasizmi?>")
choy = input('Choy olasizmi?>')
non=input("Non olasizmi?>")
salat=input("Salat olasizmi?>")
coca_cola=input("Coca-cola olasizmi?>")




if tovuq_shorva == 'ha':
    narx = narx + 15000
if choy == 'ha':
    narx = narx + 4000
if non == "ha":
    narx=narx+3000
if salat == "ha":
    narx=narx+5000
if coca_cola == "ha":
    narx=narx+5000


print(f"sizdan umumiy {narx} bo'ldi")
