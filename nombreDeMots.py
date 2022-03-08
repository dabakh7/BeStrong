def compteMots(ph):
    i = 0
    n = 0
    while i < len(ph):
        if ph[i] == " " or ph[i]==ph[len(ph)-1] :
            n = n + 1
        i = i + 1

    return n

num1 = compteMots("Samba ndiaye hg dfcrgv jhj s")
num2 = compteMots("")
print("Le nombre de mots",num1)
print("Le nombre de mots",num2)