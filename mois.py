def nomMois(n):
    if n==1:
        m = "Janvier"
    elif n==2:
        m = "Février"
    elif n==3:
        m = "Mars"
    elif n==4:
        m = "Avril"
    elif n==5:
        m = "Mai"
    elif n==6:
        m = "Juin"
    elif n==7:
        m = "Juillet"
    elif n==8:
        m = "Août"
    elif n==9:
        m = "Septembre"
    elif n==10:
        m = "Octobre"
    elif n==11:
        m = "Novembre"
    elif n==12:
        m = "Décembre"
    else:
        m = "Entrer un numéro correct"

    return m

print(nomMois(4))