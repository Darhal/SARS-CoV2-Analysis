from src.needleman import *

# Some applications of needleman_all (Bonus)
# Print arrays that have the alignements of the two sequences and the third element of the array is the alignement score
print("-----------------------------------------")
m = needleman_all("GAAT", "GGAT", [1, 0, 0])
for l in m:
    print(l)
print("-----------------------------------------")
m = needleman_all("NGNYGG", "NNYGG", cost_mat=[1, 2, 3, 2, 0, 3, 0, 0, 0, -2], key="NYG")
for l in m:
    print(l)
print("-----------------------------------------")