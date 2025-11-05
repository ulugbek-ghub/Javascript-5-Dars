# "w" - write
# "a" - append

#wb - write binary
# rb - read binary


filename = "student.txt"
# ism = "Jasur Komilov"
# height = 1.75
# tyil = 2005
# maktab = 3

# with open (filename, "w") as file:
#     file.write(ism + "\n")
#     file.write(str(height) + "\n")
#     file.write(str(tyil) + "\n")
#     file.write(str(maktab) + "\n")

with open(filename, 'a') as file:
    file.write("Kamoll Jasurov\n")
    file.write("1.80\n")
    file.write("2006\n")
    file.write("4\n")
