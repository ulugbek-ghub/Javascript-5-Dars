#1)
filename = "pi_million_digits.txt"
pi = 3.14159265359

with open(filename, "w") as file:
    print(round(pi, 3))